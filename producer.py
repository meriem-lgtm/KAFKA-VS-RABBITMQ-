from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "sensor_id": 1,
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send('sensor-data', value=data)
    print("Envoyé :", data)

    time.sleep(1)