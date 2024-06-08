from utils import * 
import time

commodities_dict = {
    "gold": "GC=F",
    "silver": "SI=F",
    "oil": "CL=F",
    "corn": "ZC=F",
    "orangejuice": "OJ=F",
}

client_name = 'stock-producer'
producer = create_producer(client_name)

while True:
    
    for topic, commoditie in commodities_dict.items():
        url = f"https://query2.finance.yahoo.com/v8/finance/chart/{commoditie}"
        fetch_url(topic, url, producer)
    
    print("\nSleeping...\n")
    time.sleep(0.5)   