# UAV Telemetry Dashboard

A real-time UAV telemetry dashboard with anomaly detection, analytics, and multiple visualizations. Built with Flask, MQTT, WebSockets, and Chart.js. Includes a modular backend, responsive frontend, and Android app integration.

## Features
- Flask backend connects to an MQTT broker and relays telemetry via WebSocket
- Real-time dashboard with three live charts: Altitude, Speed, Battery
- Analytics: min, max, average for each metric (last 20 points)
- Anomaly detection (low battery, low altitude) with alert popups and anomaly counts
- Modular, well-documented codebase
- Android app support (see mobile/ directory)
- **Dummy mode:** Demo and visualize the dashboard without any MQTT broker

## Architecture
```
[UAV/MQTT Publisher] -> [MQTT Broker] <-[Flask Backend]<-> [Web Dashboard]
                                            ^
                                            |
                                    [Android App]
```

- **MQTT Broker:** Handles telemetry messages (default: localhost:1883)
- **Flask Backend:** Subscribes to `uav/telemetry`, emits data and alerts via WebSocket
- **Web Dashboard:** Connects via Socket.IO, displays real-time charts, analytics, alerts, and latest telemetry table
- **Android App:** Connects to MQTT, displays telemetry (altitude, speed, battery)

## Visualizations & Analytics
- **Altitude, Speed, Battery:** Each has its own real-time line chart (last 20 points)
- **Latest Telemetry Table:** Shows the most recent values for all metrics
- **Analytics Table:** Shows min, max, and average for each metric (last 20 points)
- **Anomaly Counts:** Shows how many of the last 20 points triggered low battery or low altitude alerts

## Setup
### Prerequisites
- Python 3.8+
- Mosquitto MQTT broker (or any MQTT broker) [optional for full demo]
- Node.js (optional, for frontend development)

### Install Python dependencies
```
pip install -r requirements.txt
pip install eventlet
```

### Start the MQTT broker (optional)
- Install Mosquitto from https://mosquitto.org/download/
- Start the broker:
  ```
  mosquitto
  ```

### Run the backend
```
python app.py
```

- The dashboard will now automatically open in your default web browser when you run the backend. If you want to access it from a different device, open `http://localhost:5000/` manually in your browser.

### Open the dashboard

- By default, the dashboard will auto-open in your browser. If it does not, visit:

```
http://localhost:5000/
```

### Simulate telemetry data
#### **Option 1: With MQTT broker**
Publish to `uav/telemetry` topic, e.g.:
```
mosquitto_pub -h localhost -t uav/telemetry -m '{"altitude": 100, "speed": 12, "battery": 95}'
```
Or use the provided dummy script:
```
python test_mqtt_publish.py
```

#### **Option 2: Dummy mode (no MQTT broker required!)**
**Purpose:** Dummy mode allows you to demo and visualize the dashboard, analytics, and alerting features even if you do not have an MQTT broker installed or running. This is ideal for quick demos, development, or sharing the project with others.

Run the dummy script in no-broker mode:
```
python test_mqtt_publish.py --no-mqtt
```
This will POST telemetry directly to the backend, so you can demo the dashboard and all analytics/visualizations without any MQTT setup.

## Android App
- See the `mobile/` directory for Jetpack Compose app code and setup.

## Troubleshooting
- **MQTT connection refused:** Ensure the broker is running on `localhost:1883` or use dummy mode.
- **No data on dashboard:** Check backend logs for errors, verify MQTT topic and payload format, or use dummy mode.
- **Alerts not showing:** Ensure telemetry includes `battery` and `altitude` fields.

## Performance Tips
- Use Flask-SocketIO with `async_mode='eventlet'` for concurrency
- Disable Chart.js animations for fast rendering
- Use MQTT QoS 0 for low-latency delivery
- Minimize WebSocket payload size
- Use efficient state updates in Jetpack Compose

## License
MIT
