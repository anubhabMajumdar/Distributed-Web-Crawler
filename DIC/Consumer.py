from confluent_kafka import Consumer, KafkaError
from configFile import *
import readURL
from Mongodb import MongoDb
from Producer import KafkaProducer

mongo = MongoDb()
producer = KafkaProducer()

c = Consumer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'group.id': GROUP_ID})
c.subscribe([TOPIC])

running = True
while running:
    url = c.poll()
    if not url.error():
        children = readURL.getLinks(url.value())
        mongo.insert_into_graph(url.value(), children)
        producer.check_and_insert_urls(children)

c.close()