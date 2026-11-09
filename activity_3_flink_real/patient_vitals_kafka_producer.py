"""
================================================================================
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 3: REAL PATIENT TELEMETRY PRODUCER
  Student Name : Joel B John
  USN          : 1MS24CI060
  Department   : CSE (Artificial Intelligence & Machine Learning)
  Institution  : Ramaiah Institute of Technology (MSRIT)
  File         : patient_vitals_kafka_producer.py
================================================================================
Simulates IoT connected medical monitors (pulse oximeters, ECG, digital thermistors),
streaming continuous patient vital signs to real Apache Kafka broker on port 9092
for consumption by Apache Flink.
================================================================================
"""

import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

BOOTSTRAP_SERVERS = ["localhost:9092"]
TOPIC_NAME = "patient_vitals_stream_1MS24CI060"

PATIENTS = [
    {
        "patient_id": "PATIENT_1MS24CI060_01",
        "name": "Patient Alpha",
        "ward": "ICU Bed 101",
        "condition": "Post-Cardiac Surgery",
        "anomaly_prob": 0.35
    },
    {
        "patient_id": "PATIENT_1MS24CI060_02",
        "name": "Patient Beta",
        "ward": "ICU Bed 102",
        "condition": "Severe Acute Respiratory Care",
        "anomaly_prob": 0.40
    },
    {
        "patient_id": "PATIENT_1MS24CI060_03",
        "name": "Patient Gamma",
        "ward": "Step-Down Ward Bed 205",
        "condition": "Pneumonia Recovery",
        "anomaly_prob": 0.20
    },
    {
        "patient_id": "PATIENT_1MS24CI060_04",
        "name": "Patient Delta",
        "ward": "Telemetry Ward Bed 310",
        "condition": "Routine Observation",
        "anomaly_prob": 0.10
    }
]

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("       BIG DATA SYSTEMS (24CI51) - ACTIVITY 3: REAL APACHE FLINK            ")
    print("         REAL PATIENT MONITORING TELEMETRY STREAM PRODUCER (KAFKA)           ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

def generate_vital_reading(patient):
    is_anomaly = random.random() < patient["anomaly_prob"]
    if is_anomaly:
        anomaly_type = random.choice(["HR_SPIKE", "HR_DROP", "SPO2_LOW", "FEVER"])
        if anomaly_type == "HR_SPIKE":
            hr = random.randint(115, 148)
            spo2 = random.randint(93, 97)
            temp = round(random.uniform(36.8, 37.4), 1)
        elif anomaly_type == "HR_DROP":
            hr = random.randint(38, 47)
            spo2 = random.randint(92, 96)
            temp = round(random.uniform(36.5, 37.2), 1)
        elif anomaly_type == "SPO2_LOW":
            hr = random.randint(85, 115)
            spo2 = random.randint(84, 91)
            temp = round(random.uniform(36.9, 37.8), 1)
        else: # FEVER
            hr = random.randint(95, 118)
            spo2 = random.randint(93, 97)
            temp = round(random.uniform(38.7, 40.2), 1)
    else:
        hr = random.randint(62, 98)
        spo2 = random.randint(95, 99)
        temp = round(random.uniform(36.5, 37.3), 1)

    return {
        "event_time": time.time(),
        "timestamp_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "patient_id": patient["patient_id"],
        "name": patient["name"],
        "ward": patient["ward"],
        "condition": patient["condition"],
        "heart_rate": hr,
        "spo2": spo2,
        "temperature": temp
    }

def run_vitals_producer(num_events=40, delay_sec=0.5):
    print_banner()

    print(f"[*] Connecting to Kafka Broker at {BOOTSTRAP_SERVERS}...")
    try:
        producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            key_serializer=lambda k: k.encode("utf-8"),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            acks=1
        )
        print(f"[OK] Connected! Telemetry streaming to topic '{TOPIC_NAME}'\n")
    except Exception as e:
        print(f"[!] Error: {e}")
        return

    random.seed(60)

    try:
        for i in range(1, num_events + 1):
            patient = random.choice(PATIENTS)
            payload = generate_vital_reading(patient)

            producer.send(TOPIC_NAME, key=patient["patient_id"], value=payload)
            print(f"[IOT EMITTER] Event #{i:02d} | {patient['patient_id'][-2:]} | {patient['name']:<13} | HR: {payload['heart_rate']:3d} bpm | SpO2: {payload['spo2']:2d}% | Temp: {payload['temperature']:4.1f}°C")
            time.sleep(delay_sec)

        producer.flush()
        producer.close()
        print("\n[OK] Completed simulated real telemetry transmission.")

    except KeyboardInterrupt:
        print("\n[!] Producer stopped by user.")

if __name__ == "__main__":
    run_vitals_producer()
