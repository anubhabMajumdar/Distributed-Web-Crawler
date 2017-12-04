from confluent_kafka import Producer
from Mongodb import MongoDb
from configFile import *


class KafkaProducer:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})
        self.mongo = MongoDb()

    def insert_url(self, url):
        self.mongo.add_url_status(url, "enqueued")
        self.producer.produce(URL_TOPIC, url)
        self.producer.flush()
