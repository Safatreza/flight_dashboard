# Flight Dashboard — Interview Walkthrough Script

---

## 1. Project Introduction

- **Problem Solved:**  
  Flight Dashboard addresses the need for real-time monitoring and visualization of UAV (drone) telemetry data, making it easier to track key flight metrics and detect anomalies during operation.
- **Intended User:**  
  The tool is designed for UAV operators, engineers, and researchers who need a clear, live view of telemetry data for diagnostics, safety, or analytics.
- **Key Features:**  
  The dashboard provides real-time charts for altitude, speed, and battery, supports both live MQTT feeds and dummy data simulation, and includes built-in anomaly detection with alerting.

---

## 2. Architecture Overview

**High-Level Diagram:**
```
[UAV/MQTT Publisher] → [MQTT Broker] ←→ [Flask Backend] ←→ [Web Dashboard (JavaScript/Chart.js)]
                                            ↑
                                    [Dummy Data Script]
```

- **MQTT Broker:**  
  Acts as the message hub for telemetry data, typically running locally (e.g., Mosquitto).
- **Flask Backend:**  
  Subscribes to telemetry topics, processes and relays data to the frontend via WebSockets (Socket.IO), and exposes a REST endpoint for dummy data.
- **JavaScript Frontend:**  
  Connects to the backend using Socket.IO, renders real-time charts with Chart.js, and displays analytics and alerts.

---

## 3. Code Walkthrough Plan

**Key Files:**

- `app.py`  
  *Main Flask backend. Hosts the dashboard, handles both MQTT and dummy POST telemetry, emits real-time updates to the frontend.*
  - _Talking point:_ "This is the entry point for the backend. It sets up Flask, Socket.IO, and routes for both the dashboard and dummy data."

- `mqtt_handler.py`  
  *Handles MQTT connections, subscribes to telemetry, and emits data and alerts to the frontend.*
  - _Talking point:_ "This module abstracts all MQTT logic, keeping the backend modular and easy to maintain."

- `test_mqtt_publish.py`  
  *Dummy data publisher. Can send telemetry via MQTT or direct POST for demo/testing.*
  - _Talking point:_ "This script lets me simulate telemetry data, which is great for demos or development without a real drone or broker."

- `templates/index.html`  
  *Frontend dashboard. Uses JavaScript, Socket.IO, and Chart.js to display real-time data and analytics.*
  - _Talking point:_ "The frontend is a single-page app that updates live as new telemetry arrives, with charts and alert popups."

---

## 4. Demo Instructions

- **Explaining Dummy Mode:**  
  "For demo purposes, I can run the dashboard in dummy mode using a `--no-mqtt` flag. This bypasses the need for a live MQTT broker and posts simulated telemetry directly to the backend."

- **Live Demo Script:**  
  1. "First, I start the backend with `python flight_dashboard-main/app.py`. The dashboard auto-opens in my browser."
  2. "Next, I run the dummy publisher: `python flight_dashboard-main/test_mqtt_publish.py --no-mqtt`."
  3. "You'll see the charts update in real time, and if the battery or altitude drops below a threshold, alert popups appear."

---

## 5. Technical Decisions

- **Flask:**  
  Chosen for its simplicity and strong ecosystem for REST APIs and real-time features (via Flask-SocketIO).
- **MQTT:**  
  Used for lightweight, real-time telemetry transport—ideal for IoT and UAV scenarios.
- **REST API (for dummy mode):**  
  Enables easy simulation and testing without a broker, improving development speed and demo reliability.
- **Chart.js:**  
  Provides responsive, interactive charts with minimal setup, perfect for real-time data visualization.

---

## 6. Challenges & Lessons Learned

- **Asynchronous MQTT Integration:**  
  Ensuring the backend could handle both MQTT and HTTP POST data streams without blocking or race conditions.
- **Frontend Real-Time Updates:**  
  Managing efficient updates and avoiding performance issues with Chart.js and Socket.IO.
- **Error Handling & Robustness:**  
  Handling dropped MQTT connections, malformed data, and ensuring the dashboard remains responsive.
- **Modularity:**  
  Keeping MQTT logic separate from the Flask app for easier testing and future expansion.

---

## 7. Future Improvements & Integration Ideas

- **WebSocket-Only Mode:**  
  Streamline real-time updates by supporting pure WebSocket feeds for broader integration.
- **Sensor/Data Expansion:**  
  Add support for more telemetry fields or additional sensor types (e.g., GPS, IMU).
- **Database Logging:**  
  Persist telemetry and alert data for historical analysis and reporting.
- **User Authentication:**  
  Add login and role-based access for multi-user environments.

**Conclusion:**  
Flight Dashboard provides a robust, extensible foundation for real-time UAV telemetry monitoring. Its modular design, support for both live and simulated data, and clear visualization make it valuable for both operational and development use cases. The project demonstrates practical skills in Python, Flask, MQTT, and real-time web technologies, and is ready for further integration or deployment in more complex environments. 