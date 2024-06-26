from flask import Flask, render_template, Response, request, jsonify
import json
import time as time_module
from pymongo import MongoClient
from confluent_kafka.admin import AdminClient

app = Flask(__name__)

def get_all_documents_from_collection(collection_name):
    db_client = MongoClient("mongo", 27017)
    mydb = db_client["commodities_db"] 
    # documents = mydb[collection_name].find({}, {'price': 1, 'time': 1, '_id': 0}).sort("$natural").limit(100)
    documents = mydb[collection_name].find({}, {'price': 1, 'time': 1, '_id': 0}).sort("time",-1).limit(100)
    data = [{'price': float(doc['price']), 'time': doc['time']} for doc in documents]
    data.reverse()
    
    return data

def generate_data_by_commodity(topicname):
    while True:
        commodities = get_all_documents_from_collection(topicname)
        yield f"data: {json.dumps(commodities)}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    commodity = request.args.get('commodity', 'gold')
    return Response(generate_data_by_commodity(commodity), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
