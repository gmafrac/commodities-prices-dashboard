from flask import Flask, render_template, Response, request, jsonify
import json
import time as time_module
from pymongo import MongoClient
from confluent_kafka.admin import AdminClient

app = Flask(__name__)

kafka_conf = {
    'bootstrap.servers': 'kafka:9092'
}


# kafka_conf = {
#     'bootstrap.servers': 'localhost:9092'
# }
admin_client = AdminClient(kafka_conf)

def list_kafka_topics():
    metadata = admin_client.list_topics(timeout=10)
    return metadata.topics.keys()

def get_all_documents_from_collection(collection_name):
    db_client = MongoClient("mongo", 27017)
    mydb = db_client["commodities_db"]
    documents = mydb[collection_name].find({}, {'price': 1, 'time': 1, '_id': 0})
    data = [{'price': float(doc['price']), 'time': doc['time']} for doc in documents]
    return data

def generate_data_by_commoditie(topicname):
    while True:
        commodities = get_all_documents_from_collection(topicname)
        yield f"data: {json.dumps(commodities)}\n\n"
        time_module.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    commodity = request.args.get('commodity', 'gold')
    return Response(generate_data_by_commoditie(commodity), mimetype='text/event-stream')

# @app.route('/data')
# def data():
#     commodity = request.args.get('commodity', 'gold')
#     prices = get_all_documents_from_collection(commodity)
#     return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
