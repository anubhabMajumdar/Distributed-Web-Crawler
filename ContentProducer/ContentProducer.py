from confluent_kafka import Producer
from configFile import *
from Mongodb import MongoDb


class KafkaContentProducer:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})
        self.mongo = MongoDb()

    def insert_all_urls(self, urls):
        for url in urls:
            self.producer.produce(UNPROCESSED_URL_TOPIC, value=url)
        self.producer.flush()
