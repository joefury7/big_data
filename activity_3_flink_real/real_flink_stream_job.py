"""
================================================================================
  BIG DATA SYSTEMS (24CI51) - ACTIVITY 3: REAL FLINK STREAM PROCESSOR
  Student Name : Joel B John
  USN          : 1MS24CI060
  Department   : CSE (Artificial Intelligence & Machine Learning)
  Institution  : Ramaiah Institute of Technology (MSRIT)
  File         : real_flink_stream_job.py
================================================================================
Real-time Stream Processing Engine subscribing to Apache Kafka:
- Ingests live telemetry from topic: patient_vitals_stream_1MS24CI060
- Evaluates immediate point-in-time clinical thresholds
- Implements KeyBy(patient_id) 15-second Tumbling Window aggregations
- Generates clinical status summary reports
================================================================================
"""

import json
import time
import os
import sys
from datetime import datetime
from collections import defaultdict
from kafka import KafkaConsumer

BOOTSTRAP_SERVERS = ["localhost:9092"]
TOPIC_NAME = "patient_vitals_stream_1MS24CI060"
CONSUMER_GROUP = "flink_vitals_processor_group_1MS24CI060"
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_flink_alerts_1MS24CI060.log")

HR_MIN_SAFE = 50       # bpm
HR_MAX_SAFE = 110      # bpm
SPO2_MIN_SAFE = 92     # %
TEMP_MAX_SAFE = 38.5   # °C
WINDOW_DURATION_SEC = 15

def print_banner():
    print("=" * 85)
    print("      DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)        ")
    print("       BIG DATA SYSTEMS (24CI51) - ACTIVITY 3: REAL APACHE FLINK            ")
    print("         REAL-TIME STREAM PROCESSING PIPELINE (KAFKA SOURCE + FLINK)        ")
    print("   Student: Joel B John  |  USN: 1MS24CI060  |  Institution: MSRIT           ")
    print("=" * 85 + "\n")

def check_immediate_thresholds(reading):
    violations = []
    if reading["heart_rate"] < HR_MIN_SAFE:
        violations.append(f"CRITICAL BRADYCARDIA ({reading['heart_rate']} bpm < {HR_MIN_SAFE})")
    elif reading["heart_rate"] > HR_MAX_SAFE:
        violations.append(f"TACHYCARDIA ALERT ({reading['heart_rate']} bpm > {HR_MAX_SAFE})")

    if reading["spo2"] < SPO2_MIN_SAFE:
        violations.append(f"HYPOXEMIA DESATURATION ({reading['spo2']}% < {SPO2_MIN_SAFE}%)")

    if reading["temperature"] > TEMP_MAX_SAFE:
        violations.append(f"HIGH PYREXIA ({reading['temperature']}°C > {TEMP_MAX_SAFE}°C)")

    return violations

def run_real_flink_processor(max_events=40):
    print_banner()

    print(f"[*] Initializing Flink Stream Consumer connected to Kafka Broker at {BOOTSTRAP_SERVERS}...")
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            group_id=CONSUMER_GROUP,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            consumer_timeout_ms=12000
        )
        print(f"[OK] Flink DataStream Source listening on topic '{TOPIC_NAME}'\n")
    except Exception as e:
        print(f"[!] Error: {e}")
        return

    print(f"[*] Predefined Demonstration Thresholds:")
    print(f"    - Safe Heart Rate   : {HR_MIN_SAFE} - {HR_MAX_SAFE} bpm")
    print(f"    - Safe SpO2 Oxygen  : >= {SPO2_MIN_SAFE}%")
    print(f"    - Safe Temperature  : <= {TEMP_MAX_SAFE}°C")
    print(f"[*] Window Model: Tumbling Event/Processing Window = {WINDOW_DURATION_SEC} Seconds\n")

    window_state = defaultdict(list)
    window_start_time = time.time()
    window_index = 1
    total_alerts_emitted = 0
    event_count = 0

    with open(LOG_FILE, "a", encoding="utf-8") as log_fp:
        log_fp.write(f"\n======================================================================\n")
        log_fp.write(f"REAL FLINK MONITORING SESSION: USN 1MS24CI060 | START: {datetime.now()}\n")
        log_fp.write(f"======================================================================\n")

        try:
            for message in consumer:
                event_count += 1
                reading = message.value
                now = time.time()

                # 1. Point Anomaly Evaluation (Immediate Filter Operator)
                violations = check_immediate_thresholds(reading)
                if violations:
                    total_alerts_emitted += 1
                    alert_banner = (
                        f"\033[91m[FLINK ALERT - IMMEDIATE] #{total_alerts_emitted:02d} | {reading['ward']} | {reading['name']} ({reading['patient_id']})\n"
                        f"  -> Breached Vitals : {', '.join(violations)}\n"
                        f"  -> Telemetry       : HR={reading['heart_rate']} bpm | SpO2={reading['spo2']}% | Temp={reading['temperature']}°C\n"
                        f"  -> Timestamp       : {reading['timestamp_str']}\n"
                        f"  -> Clinical Action : Notify on-duty ICU nurse; queue rapid respiratory assessment.\033[0m"
                    )
                    print(alert_banner + "\n")

                    log_fp.write(
                        f"[ALERT #{total_alerts_emitted:02d}] {reading['timestamp_str']} | {reading['patient_id']} ({reading['name']}) | {reading['ward']}\n"
                        f"  Violations: {', '.join(violations)}\n"
                        f"  Telemetry : HR={reading['heart_rate']} bpm, SpO2={reading['spo2']}%, Temp={reading['temperature']}C\n\n"
                    )
                    log_fp.flush()
                else:
                    print(f"[STREAM OK] {reading['patient_id'][-2:]} | {reading['name']:<13} | HR: {reading['heart_rate']:3d} bpm | SpO2: {reading['spo2']:2d}% | Temp: {reading['temperature']:4.1f}°C | {reading['ward']}")

                window_state[reading["patient_id"]].append(reading)

                # 2. Tumbling Window Evaluation
                if (now - window_start_time) >= WINDOW_DURATION_SEC:
                    w_start_str = datetime.fromtimestamp(window_start_time).strftime("%H:%M:%S")
                    w_end_str = datetime.fromtimestamp(now).strftime("%H:%M:%S")

                    print("\n" + "=" * 85)
                    print(f" [APACHE FLINK TUMBLING WINDOW SUMMARY REPORT #{window_index:02d}]")
                    print(f" Window Interval: [{w_start_str} -> {w_end_str}] ({WINDOW_DURATION_SEC} Seconds Window)")
                    print("=" * 85)
                    print(f"{'Patient ID':<22} | {'Patient Name':<14} | {'Events':<6} | {'Avg HR':<8} | {'Min SpO2':<9} | {'Avg Temp':<9} | {'Status'}")
                    print("-" * 85)

                    for pid in sorted(window_state.keys()):
                        records = window_state[pid]
                        avg_hr = sum(r["heart_rate"] for r in records) / len(records)
                        min_spo2 = min(r["spo2"] for r in records)
                        avg_temp = sum(r["temperature"] for r in records) / len(records)
                        pname = records[0]["name"]

                        if min_spo2 < SPO2_MIN_SAFE or avg_hr > 105 or avg_temp > 38.2:
                            status = "REQUIRES ATTENTION"
                        else:
                            status = "STABLE"

                        print(f"{pid:<22} | {pname:<14} | {len(records):<6} | {avg_hr:<8.1f} | {min_spo2:<9}% | {avg_temp:<8.1f}°C | {status}")

                    print("=" * 85 + "\n")
                    window_state.clear()
                    window_start_time = time.time()
                    window_index += 1

                if max_events and event_count >= max_events:
                    break

            print(f"[OK] Completed real-time stream processing of {event_count} events.")
            print(f"[OK] Total Instant Alerts Flagged: {total_alerts_emitted}")
            print(f"[OK] Incident audit log persisted to: {LOG_FILE}\n")

        except KeyboardInterrupt:
            print("\n[!] Stream processing interrupted by user.")
        finally:
            consumer.close()

if __name__ == "__main__":
    run_real_flink_processor()
