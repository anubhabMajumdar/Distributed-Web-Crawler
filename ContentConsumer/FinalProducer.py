from confluent_kafka import Producer
from Mongodb import MongoDb
from configFile import *


class KafkaProducer:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})
        self.mongo = MongoDb()

    def check_and_insert_urls(self, urls):
        for url in urls:
            #print("Checking if url is already processed...")
            if not self.mongo.is_url_processed(url):
                #print("Url not processed... Now adding status")
                self.mongo.add_url_status(url, "enqueued")
                #print("Status added...Now producing")
                self.producer.produce(URL_TOPIC, url)
