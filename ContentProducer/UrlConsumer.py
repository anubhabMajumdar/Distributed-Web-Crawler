from confluent_kafka import Consumer
from configFile import *
from ContentProducer import KafkaContentProducer
from URLReader import UrlReader
from Mongodb import MongoDb
import time

kafka_url_producer = KafkaContentProducer()
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
        print("Checking if already processed...")
        if mongodb.is_already_in_wikigraph(url.value()):
            print("Url was already processed")
            mongodb.add_url_status(url.value(), "processed")
        else:
            mongodb.add_url_status(url.value(), "processed")
            content = url_reader.get_content(url.value())
            urls = url_reader.parse_content(content)
            print("Found number of children urls - " + str(len(urls)))
            mongodb.insert_into_graph(url.value(), urls)
            kafka_url_producer.insert_all_urls(urls)
            sec = 25
            print("Sleeping for " + str(sec) + "seconds")
            time.sleep(sec)
c.close()
