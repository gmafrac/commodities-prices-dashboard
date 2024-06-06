from flask import Flask, render_template, Response
import json
import time
import random
from pymongo import MongoClient
from confluent_kafka.admin import AdminClient

app = Flask(__name__)

kafka_conf = {
    'bootstrap.servers': 'localhost:9092'
}
admin_client = AdminClient(kafka_conf)


def list_kafka_topics():
    metadata = admin_client.list_topics(timeout=10)
    return metadata.topics.keys()


def get_all_documents_from_collection(collection_name):
    db_client = MongoClient("localhost", 27017)
    mydb = db_client["commodities_db"]
    prices = [float(doc['price']) for doc in mydb[collection_name].find({}, {'price': 1, '_id': 0})]
    prices = json.dumps(prices)    
    return prices


def generate_data_by_commoditie(topicname):

    while True:
        commodities = get_all_documents_from_collection(topicname) 
        yield f"data: {commodities}\n\n"
        time.sleep(2)  

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/commoditie/<topicname>')
# def get_commoditie(topicname):

#     available_topics = list_kafka_topics()
#     if topicname not in available_topics:
#         return f"Commoditie {topicname} not found", 404
#     print(generate_data_by_commoditie(topicname))
#     return render_template('index.html', topicname=topicname)
    

@app.route('/stream')
def stream():
    topicname = 'stock-producer'
    return Response(generate_data_by_commoditie('gold'), mimetype='text/event-stream')
    
if __name__ == '__main__':
    app.run(debug=True)