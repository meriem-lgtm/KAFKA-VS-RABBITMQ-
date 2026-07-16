from kafka import KafkaProducer, KafkaConsumer
import json
import time
import threading

TOPIC = "benchmark_topic"

# ---------- CONSUMER ----------
received = 0
start_time = None

def consumer_job():
    global received, start_time

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    for msg in consumer:
        if start_time is None:
            start_time = time.time()

        received += 1

        if received == 1000:
            end_time = time.time()
            print("\nKafka Results:")
            print("Time:", end_time - start_time)
            print("Messages/sec:", 1000 / (end_time - start_time))
            break

# ---------- PRODUCER ----------
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

threading.Thread(target=consumer_job, daemon=True).start()

time.sleep(2)

for i in range(1000):
    producer.send(TOPIC, {"id": i})

producer.flush()

time.sleep(5)