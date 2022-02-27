import traceback
from kafka import KafkaProducer
from kafka.errors import KafkaError

topic = 'class.test.1'

producer = KafkaProducer(bootstrap_servers='abkhan.tplinkdns.com:9092')
try:
    state = producer.send(topic, b'Hello, World!')
    record_metadata = state.get(timeout=10)
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)
except KafkaError as err:
    traceback.print_exc()

#ret = producer.send('class.test.1', key=b'message-two', value=b'This is Kafka-Python')
#print(ret)
