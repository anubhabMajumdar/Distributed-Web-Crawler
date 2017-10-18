from confluent_kafka import Producer
from Mongodb import MongoDb
from configFile import *


class KafkaProducer:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})
        self.mongo = MongoDb()

    def check_and_insert_urls(self, urls):
        for url in urls:
            if self.mongo.is_url_processed(url) == False:
                self.mongo.add_url_status(url, "enqueued")
                self.producer.produce(TOPIC, url)
        self.producer.flush()
