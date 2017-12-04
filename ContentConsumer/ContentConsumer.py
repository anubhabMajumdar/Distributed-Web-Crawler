print ("Program Started")
from confluent_kafka import Consumer
from configFile import *
from FinalProducer import KafkaProducer
from URLReader import UrlReader
from Mongodb import MongoDb

producer = KafkaProducer()
url_reader = UrlReader()
mongodb = MongoDb()

c = Consumer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'group.id': GROUP_CONTENT_CONSUMER})#, 'max.partition.fetch.bytes': 200000000, 'receive.message.max.bytes': 1000000000});
c.subscribe([UNPROCESSED_URL_TOPIC])

running = True
while running:
    print("Waiting for unprocessed url to be fetched")
    data = c.poll()
    if not data.error():
        url = data.value()
        print("Fetched url from Kafka - " + str(url))
        print("Checking if this url is already processed...")
        if mongodb.is_url_processed(url):
            print("Url already processed... Skipping it")
        else:
            print("Url not processed.... adding to the topic")
            producer.insert_url(url)
c.close()
