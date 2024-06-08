from pymongo import MongoClient
from confluent_kafka import Consumer, KafkaError
from datetime import datetime

commodities_dict = {
    "gold": "GC=F",
    "silver": "SI=F",
    "oil": "CL=F",
    "corn": "ZC=F",
    "orangejuice": "OJ=F",
}
 
CONFIG = {
    'bootstrap.servers': "kafka:9092",
    'group.id': "my-group",
    'auto.offset.reset': 'earliest'
}

def create_collections():
    
    db_client = MongoClient("mongo", 27017)
    
    db = db_client["commodities_db"]
    collections = {}
    for topic in commodities_dict.keys():
        collections[topic] = db[topic]
        
    return collections

def create_consumer(topic):
    
    consumer = Consumer(CONFIG)
    consumer.subscribe([topic])
    return consumer

def create_consumers():
    
    consumers = {}
    for topic in commodities_dict.keys():
        consumers[topic] = create_consumer(topic)
        
    return consumers

def get_message(topic, consumers, collections):
    
    msg = consumers[topic].poll(1.0)
    
    if msg is None:
        return None
            
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}')
            return False
    else:
        print(f"The message has been received: {msg.value().decode('utf-8')}")
        
        data_price = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg.value().decode('utf-8')]        
    
        collections[topic].insert_one({
            "time": data_price[0], 
            "price": data_price[1]
            })
        
        print(f"The message has been saved to the collection {topic}: \n{data_price}\n")

    return True