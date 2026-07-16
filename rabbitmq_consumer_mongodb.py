import pika
import json
from pymongo import MongoClient

# MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["streaming_db"]
collection = db["rabbitmq_data"]

# RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='sensor_queue')

print("RabbitMQ Consumer -> MongoDB started")

def callback(ch, method, properties, body):

    data = json.loads(body)

    collection.insert_one(data)

    print("Inserted:", data)

channel.basic_consume(
    queue='sensor_queue',
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()