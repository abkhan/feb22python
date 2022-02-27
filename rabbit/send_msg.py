# example_publisher.py
import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = "amqp://abkhan:abkhan@abkhan.tplinkdns.com:5672"
credentials = pika.PlainCredentials('iccuser', 'iccuser')
params = pika.ConnectionParameters('abkhan.tplinkdns.com', 5672, '/', credentials)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
# send a message

channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')
print ("[x] Message sent to consumer")
connection.close()

