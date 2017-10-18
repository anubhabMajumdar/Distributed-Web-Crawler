from confluent_kafka import Consumer, KafkaError
import configFile
from configFile import *

c = Consumer({'bootstrap.servers': BOOTSTRAP_SERVERS, 'group.id': GROUP_ID})
c.subscribe([TOPIC])

running = True
while running:
    msg = c.poll()
    if not msg.error():
        print('Received message: %s' % msg.value().decode('utf-8'))
c.close()