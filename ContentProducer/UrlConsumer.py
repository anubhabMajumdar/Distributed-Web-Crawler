from confluent_kafka import Consumer
from configFile import *
from ContentProducer import KafkaContentProducer
from URLReader import UrlReader
from Mongodb import MongoDb
import time

kafka_content_producer = KafkaContentProducer()
url_reader = UrlReader()
mongodb = MongoDb()

c = Consumer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'group.id': GROUP_URL_CONSUMER})
c.subscribe([URL_TOPIC])

running = True
while running:
    print("Waiting for url to be fetched")
    url = c.poll()
    if not url.error():
        print("Fetched Url from Kafka - " + url.value())
        content = url_reader.get_content(url.value())
        mongodb.add_url_status(url.value(), "fetched")
        kafka_content_producer.insert_content(url.value(), content)
        sec = 35
        print("Sleeping for " + str(35) + "seconds")
        time.sleep(sec)
c.close()
