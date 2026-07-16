import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sensor_queue')

def callback(ch, method, properties, body):
    print("Consumer 2:", json.loads(body))

channel.basic_consume(queue='sensor_queue', on_message_callback=callback, auto_ack=True)

print("Consumer 2 started")
channel.start_consuming()