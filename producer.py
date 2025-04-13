
import pika , uuid , time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while KeyboardInterrupt:
    message = uuid.uuid4()
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=str(message))
    time.sleep(2)

connection.close()