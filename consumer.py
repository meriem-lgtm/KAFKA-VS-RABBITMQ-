import pika
import json
import csv
import os

os.makedirs("data", exist_ok=True)
file_path = "data/rabbitmq_data.csv"

# créer fichier si n'existe pas
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sensor_id", "temperature", "humidity", "timestamp"])

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='sensor_queue')

def callback(ch, method, properties, body):
    data = json.loads(body)

    print("Reçu :", data)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            data["sensor_id"],
            data["temperature"],
            data["humidity"],
            data["timestamp"]
        ])

channel.basic_consume(queue='sensor_queue', on_message_callback=callback, auto_ack=True)

print("Consumer en attente...")
channel.start_consuming()