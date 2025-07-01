import random
import time
import json
import sys

try:
    import paho.mqtt.publish as publish
except ImportError:
    publish = None

import requests

BROKER = 'localhost'
TOPIC = 'uav/telemetry'
BACKEND_URL = 'http://localhost:5000/_dummy_telemetry'  # New endpoint for direct POST

USE_DIRECT_POST = '--no-mqtt' in sys.argv or publish is None

print("Starting dummy telemetry publisher. Press Ctrl+C to stop.")
print(f"Mode: {'Direct POST to backend' if USE_DIRECT_POST else 'MQTT publish'}")

try:
    while True:
        # Generate random telemetry data
        data = {
            'altitude': round(random.uniform(0, 150), 2),
            'speed': round(random.uniform(0, 30), 2),
            'battery': round(random.uniform(0, 100), 2)
        }
        payload = json.dumps(data)
        print(f"Publishing: {payload}")
        if USE_DIRECT_POST:
            try:
                requests.post(BACKEND_URL, json=data, timeout=2)
            except Exception as e:
                print(f"[WARN] Failed to POST to backend: {e}")
        else:
            try:
                publish.single(TOPIC, payload, hostname=BROKER)
            except Exception as e:
                print(f"[WARN] MQTT publish failed: {e}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nStopped dummy telemetry publisher.") 