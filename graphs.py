import matplotlib.pyplot as plt
import numpy as np
import benchmark_results as br

systems = ["Kafka", "RabbitMQ"]

time = [br.kafka_time, br.rabbit_time]
speed = [br.kafka_speed, br.rabbit_speed]

# Graph 1 : Temps
plt.figure()
plt.bar(systems, time, color=['blue','orange'])
plt.title("Comparison of Processing Time (1000 messages)")
plt.ylabel("Time (seconds)")
plt.xlabel("System")
plt.show()

# Graph 2 : Débit
plt.figure()
plt.bar(systems, speed, color=['green','red'])
plt.title("Messages per Second Comparison")
plt.ylabel("Messages/sec")
plt.xlabel("System")
plt.show()

# Graph combiné
x = np.arange(len(systems))
plt.figure()
plt.bar(x - 0.2, time, 0.4, label="Time (s)")
plt.bar(x + 0.2, speed, 0.4, label="Messages/sec")
plt.xticks(x, systems)
plt.title("Kafka vs RabbitMQ Benchmark Comparison")
plt.legend()
plt.show()



plt.savefig("time_comparison.png")
plt.savefig("throughput_comparison.png")
plt.savefig("combined_comparison.png")
