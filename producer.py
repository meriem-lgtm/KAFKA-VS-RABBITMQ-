import pika
import json
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sensor_queue')

while True:
    data = {
        "sensor_id": 1,
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    channel.basic_publish(
        exchange='',
        routing_key='sensor_queue',
        body=json.dumps(data)
    )

    print("Envoyé :", data)
    time.sleep(1)