from kafka import KafkaConsumer

server = 'abkhan.tplinkdns.com:9092'
topic = 'class.test.1'

consumer = KafkaConsumer(
            bootstrap_servers=server,
            auto_offset_reset='earliest'
        )
consumer.subscribe([topic])

#consumer = KafkaConsumer('class.test.1', bootstrap_servers=server)
for message in consumer:
    print (message)
