from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["streaming_db"]
collection = db["kafka_data"]

# Kafka
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Kafka Consumer -> MongoDB started")

for message in consumer:
    data = message.value

    collection.insert_one(data)

    print("Inserted:", data)