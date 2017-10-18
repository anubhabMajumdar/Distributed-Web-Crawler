from confluent_kafka import Consumer, KafkaError

c = Consumer({'bootstrap.servers': '54.164.85.141', 'group.id': "local"})
c.subscribe(['karan1'])
running = True
while running:
    msg = c.poll()
    if not msg.error():
        print('Received message: %s' % msg.value().decode('utf-8'))
    elif msg.error().code() != KafkaError._PARTITION_EOF:
        print(msg.error())
        running = False
c.close()