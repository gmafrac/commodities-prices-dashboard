from utils import *

COLLECTION_NAME = "commodities"

collections = create_collections()
consumers = create_consumers()

while True:
    for topic in commodities_dict:
        ok = get_message(topic, consumers, collections)
        if ok is False:
            break