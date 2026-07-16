import pika
import json
import time
import threading

QUEUE = "benchmark_queue"

received = 0
start_time = None

# ---------- CONSUMER ----------
def consumer_job():
    global received, start_time

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE)

    def callback(ch, method, properties, body):
        global received, start_time

        if start_time is None:
            start_time = time.time()

        received += 1

        if received == 1000:
            end_time = time.time()
            print("\nRabbitMQ Results:")
            print("Time:", end_time - start_time)
            print("Messages/sec:", 1000 / (end_time - start_time))

    channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

# ---------- PRODUCER ----------
threading.Thread(target=consumer_job, daemon=True).start()

time.sleep(2)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

for i in range(1000):
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE,
        body=json.dumps({"id": i})
    )

connection.close()