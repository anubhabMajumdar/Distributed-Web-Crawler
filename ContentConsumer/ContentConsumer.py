print ("Program Started")
from confluent_kafka import Consumer
from configFile import *
from FinalProducer import KafkaProducer
from URLReader import UrlReader
from Mongodb import MongoDb

producer = KafkaProducer()
url_reader = UrlReader()
mongodb = MongoDb()

c = Consumer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'group.id': GROUP_CONTENT_CONSUMER, 'max.partition.fetch.bytes': 100000000})
c.subscribe([CONTENT_TOPIC])

running = True
while running:
    print("Waiting for content to be fetched")
    data = c.poll()
    if not data.error():
        url = data.key()
        content = data.value()
        print("Fetched Content from Kafka for url - " + str(url))
        urls = url_reader.parse_content(content)
        mongodb.add_url_status(url, "processed")
        mongodb.insert_into_graph(url, urls)
        print("Total urls - " + str(url.__len__()))
        print("Going to produce children urls now...")
        producer.check_and_insert_urls(urls)
c.close()
