"""
================================================================================
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 2: REAL APACHE KAFKA CONSUMER
  Student Name : Joel B John
  USN          : 1MS24CI060
  Department   : CSE (Artificial Intelligence & Machine Learning)
  Institution  : Ramaiah Institute of Technology (MSRIT)
  File         : real_kafka_consumer.py
================================================================================
Production Kafka Consumer subscribing to real Apache Kafka broker (localhost:9092):
- Evaluates real-time speed & vehicle count thresholds
- Commits offsets to internal topic __consumer_offsets
- Logs incident alerts to disk
================================================================================
"""

import json
import os
import sys
from datetime import datetime
from kafka import KafkaConsumer

BOOTSTRAP_SERVERS = ["localhost:9092"]
TOPIC_NAME = "traffic_telemetry_1MS24CI060"
CONSUMER_GROUP = "traffic_monitoring_group_1MS24CI060"
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_traffic_alerts_1MS24CI060.log")

SPEED_CRITICAL_THRESHOLD = 15.0   # km/h
SPEED_WARNING_THRESHOLD  = 25.0   # km/h
VEHICLE_COUNT_THRESHOLD  = 60     # vehicles

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("       BIG DATA SYSTEMS (24CI51) - ACTIVITY 2: REAL APACHE KAFKA            ")
    print("         REAL APACHE KAFKA BROKER (PORT 9092) - TELEMETRY CONSUMER          ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

def run_real_consumer(max_messages=None):
    print_banner()

    print(f"[*] Connecting to REAL Apache Kafka Cluster at {BOOTSTRAP_SERVERS}...")
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            group_id=CONSUMER_GROUP,
            auto_offset_reset="earliest",  # Replay from beginning if no offset exists
            enable_auto_commit=True,
            auto_commit_interval_ms=1000,
            key_deserializer=lambda k: k.decode("utf-8") if k else None,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            consumer_timeout_ms=10000
        )
        print(f"[OK] Subscribed to topic '{TOPIC_NAME}' via Consumer Group '{CONSUMER_GROUP}'\n")
    except Exception as e:
        print(f"[!] Error connecting to Kafka Broker: {e}")
        print("[!] Please ensure real Kafka is running on localhost:9092.")
        return

    print(f"[*] Predefined Congestion Rules:")
    print(f"    - CRITICAL ALERT : Vehicle Count > {VEHICLE_COUNT_THRESHOLD} AND Speed < {SPEED_CRITICAL_THRESHOLD} km/h")
    print(f"    - WARNING ALERT  : Vehicle Count > {VEHICLE_COUNT_THRESHOLD} AND Speed < {SPEED_WARNING_THRESHOLD} km/h")
    print(f"[*] Incident alerts logged to: {LOG_FILE}\n")

    alert_count = 0
    msg_count = 0

    with open(LOG_FILE, "a", encoding="utf-8") as log_fp:
        log_fp.write(f"\n--- REAL KAFKA STREAM SESSION: USN 1MS24CI060 | START: {datetime.now()} ---\n")

        try:
            for message in consumer:
                msg_count += 1
                payload = message.value
                part = message.partition
                offset = message.offset
                key = message.key

                v_count = payload["vehicle_count"]
                speed = payload["avg_speed_kmh"]
                junction = payload["junction_name"]
                sensor_id = payload["sensor_id"]
                t_stamp = payload["timestamp"]

                # Threshold Detection
                if v_count > VEHICLE_COUNT_THRESHOLD and speed < SPEED_CRITICAL_THRESHOLD:
                    alert_count += 1
                    alert_text = (
                        f"[ALERT - CRITICAL CONGESTION] #{alert_count:02d}\n"
                        f"  Junction  : {junction} ({sensor_id})\n"
                        f"  Metrics   : {v_count} Vehicles (Threshold > {VEHICLE_COUNT_THRESHOLD}) | Avg Speed: {speed} km/h (< {SPEED_CRITICAL_THRESHOLD} km/h)\n"
                        f"  Kafka Pos : Partition {part}, Offset {offset} | Time: {t_stamp}\n"
                        f"  Action    : Dispatching traffic warden to {junction}; Triggering signal cycle extension."
                    )
                    print(f"\033[91m{alert_text}\033[0m\n")
                    log_fp.write(alert_text + "\n\n")
                    log_fp.flush()

                elif v_count > VEHICLE_COUNT_THRESHOLD and speed < SPEED_WARNING_THRESHOLD:
                    alert_count += 1
                    alert_text = (
                        f"[ALERT - WARNING CONGESTION] #{alert_count:02d}\n"
                        f"  Junction  : {junction} ({sensor_id})\n"
                        f"  Metrics   : {v_count} Vehicles | Avg Speed: {speed} km/h (< {SPEED_WARNING_THRESHOLD} km/h)\n"
                        f"  Kafka Pos : Partition {part}, Offset {offset} | Time: {t_stamp}\n"
                        f"  Action    : Traffic advisory broadcasted to regional control room."
                    )
                    print(f"\033[93m{alert_text}\033[0m\n")
                    log_fp.write(alert_text + "\n\n")
                    log_fp.flush()

                else:
                    print(f"[STATUS: NORMAL FLOW] Part {part} Off {offset} | {sensor_id[-12:]} | {v_count:02d} veh | {speed:4.1f} km/h | {junction}")

                if max_messages and msg_count >= max_messages:
                    break

        except KeyboardInterrupt:
            print("\n[!] Consumer stopped by user.")
        finally:
            consumer.close()

if __name__ == "__main__":
    run_real_consumer()
