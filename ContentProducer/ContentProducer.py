from confluent_kafka import Producer
from configFile import *
from Mongodb import MongoDb


class KafkaContentProducer:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'message.max.bytes' :  100000000})
        self.mongo = MongoDb()

    def insert_content(self, url, content):
        self.mongo.add_url_status(url, "fetched")
        self.producer.produce(CONTENT_TOPIC, key=url, value=content)
        self.producer.flush()
