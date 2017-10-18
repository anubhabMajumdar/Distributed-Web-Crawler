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
    print("Waiting for url to be fetched")
    url = c.poll()
    if not url.error():
        print("Fetched Url from Kafka - " + url.value())
        children = readURL.getLinks(url.value())
        #print("All children of " + url.value() + " - " + str(children))
        mongo.insert_into_graph(url.value(), children)
        mongo.add_url_status(url.value(), "processed")
        print("Going to produce now...")
        producer.check_and_insert_urls(children)

c.close()
