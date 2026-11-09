"""
================================================================================
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 2: REAL APACHE KAFKA PRODUCER
  Student Name : Joel B John
  USN          : 1MS24CI060
  Department   : CSE (Artificial Intelligence & Machine Learning)
  Institution  : Ramaiah Institute of Technology (MSRIT)
  File         : real_kafka_producer.py
================================================================================
Production Kafka Producer publishing live IoT traffic sensor events to a
real Apache Kafka broker (KRaft mode) on localhost:9092.
================================================================================
"""

import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

BOOTSTRAP_SERVERS = ["localhost:9092"]
TOPIC_NAME = "traffic_telemetry_1MS24CI060"

JUNCTIONS = [
    {
        "sensor_id": "SENSOR_1MS24CI060_MSR_GATE",
        "junction_name": "MSRIT Main Gate (Mathikere)",
        "congest_prob": 0.40
    },
    {
        "sensor_id": "SENSOR_1MS24CI060_YESHWANTHPUR",
        "junction_name": "Yeshwanthpur Junction",
        "congest_prob": 0.50
    },
    {
        "sensor_id": "SENSOR_1MS24CI060_HEBBAL",
        "junction_name": "Hebbal Flyover Junction",
        "congest_prob": 0.35
    },
    {
        "sensor_id": "SENSOR_1MS24CI060_BEL_CIRCLE",
        "junction_name": "BEL Circle Cross",
        "congest_prob": 0.20
    },
    {
        "sensor_id": "SENSOR_1MS24CI060_MATHIKERE",
        "junction_name": "Mathikere Post Office Cross",
        "congest_prob": 0.25
    }
]

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("       BIG DATA SYSTEMS (24CI51) - ACTIVITY 2: REAL APACHE KAFKA            ")
    print("          REAL APACHE KAFKA BROKER (PORT 9092) - TELEMETRY PRODUCER          ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

def run_real_producer(num_events=30, delay_sec=0.6):
    print_banner()

    print(f"[*] Connecting to REAL Apache Kafka Cluster at {BOOTSTRAP_SERVERS}...")
    try:
        producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            key_serializer=lambda k: k.encode("utf-8"),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            acks="all",            # Wait for all in-sync replicas to acknowledge
            retries=3,
            linger_ms=10
        )
        print(f"[OK] Connected successfully to Kafka Broker!\n")
    except Exception as e:
        print(f"[!] Error connecting to Kafka Broker: {e}")
        print("[!] Please ensure real Kafka is started via 'bash start_real_kafka.sh' or 'powershell run_activity_2_real.ps1'.")
        return

    print(f"[*] Publishing {num_events} telemetry events to topic '{TOPIC_NAME}'...")
    print(f"[*] Key Partitioning: sensor_id hashes to specific Kafka partition.\n")

    random.seed(60)

    try:
        for i in range(1, num_events + 1):
            junction = random.choice(JUNCTIONS)
            is_rush = random.random() < junction["congest_prob"]

            if is_rush:
                vehicle_count = random.randint(62, 115)
                avg_speed = round(random.uniform(5.0, 19.5), 1)
            else:
                vehicle_count = random.randint(15, 55)
                avg_speed = round(random.uniform(28.0, 62.0), 1)

            payload = {
                "event_id": f"EVT_060_{i:05d}",
                "sensor_id": junction["sensor_id"],
                "junction_name": junction["junction_name"],
                "vehicle_count": vehicle_count,
                "avg_speed_kmh": avg_speed,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            key_str = junction["sensor_id"]

            # Asynchronous send to real Kafka topic with callback/future
            future = producer.send(TOPIC_NAME, key=key_str, value=payload)
            metadata = future.get(timeout=10)  # Block until acknowledged by broker

            print(f"[KAFKA ACK] Event #{i:03d} -> Topic: {metadata.topic} | Part: {metadata.partition} | Offset: {metadata.offset} | Key: {key_str[-12:]} | Veh: {payload['vehicle_count']:03d} | Spd: {payload['avg_speed_kmh']:4.1f} km/h")
            time.sleep(delay_sec)

        producer.flush()
        producer.close()
        print("\n[OK] Completed simulated real Kafka telemetry transmission.")

    except KeyboardInterrupt:
        print("\n[!] Producer stopped by user.")
    except Exception as e:
        print(f"[!] Kafka Producer Exception: {e}")

if __name__ == "__main__":
    run_real_producer()
