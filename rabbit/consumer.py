# example_consumer.py
import pika, os, time

def pdf_process_function(msg):
  print(" PDF processing")
  print(" [x] Received " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" PDF processing finished")
  return

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://iccuser@abkhan.tplink.com:5672/')
#url = "amqp://some:someabkhan@abkhan.tplinkdns.com:5672"
url = "amqp://asome:bkhan:asomebkhan@abkhan.tplinkdns.com:5672"
credentials = pika.PlainCredentials('update', 'update')
params = pika.ConnectionParameters('abkhan.tplinkdns.com', 5672, '/', credentials)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
print("channel started")

channel.queue_declare(queue='pdfprocess') # Declare a queue
print("q declared")

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  pdf_process_function(body)

# set up subscription on the queue
channel.basic_consume('pdfprocess',
  callback,
  auto_ack=True)

print("start consuming")
# start consuming (blocks)
channel.start_consuming()
connection.close()

