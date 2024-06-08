from confluent_kafka import Producer
import requests
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/json',
}

CONFIG = {
    'bootstrap.servers': "kafka:9092",
    'request.timeout.ms': 60000
}


def create_producer(client_name):
    CONFIG['client.id'] = client_name
    return Producer(CONFIG)

def fetch_url(topic, url, producer):
    try:
        data = requests.get(url, headers=HEADERS).json()
        
        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        producer.produce(topic, value=str(price))
        print(f"Sent stock price {price} to topic {topic}")
        producer.flush()
        
    except Exception as e:
        print(f"Failed to send stock price to topic {topic} {e}")
