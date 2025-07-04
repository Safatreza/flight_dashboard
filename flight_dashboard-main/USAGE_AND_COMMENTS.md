# UAV Telemetry Dashboard — Usage & Comments

**Note:** All commands below use explicit relative paths, so you can run them from anywhere inside the project directory.

---

## 1. Setup & Installation

```sh
# Install Python dependencies (from project root or any subdirectory)
pip install -r flight_dashboard-main/requirements.txt
pip install eventlet
```

---

## 2. Running the Backend (Dashboard Server)

```sh
python flight_dashboard-main/app.py
```
- The dashboard will automatically open in your default web browser at [http://localhost:5000/](http://localhost:5000/).

---

## 3. Simulating Telemetry Data (Dummy Mode)

```sh
python flight_dashboard-main/test_mqtt_publish.py --no-mqtt
```
- This sends random telemetry data directly to the backend for demo/testing (no MQTT broker required).

---

## 4. Simulating Telemetry Data (With MQTT Broker)

Start a local MQTT broker (optional):
```sh
mosquitto
```

Then run:
```sh
python flight_dashboard-main/test_mqtt_publish.py
```
- Or publish manually:
```sh
mosquitto_pub -h localhost -t uav/telemetry -m '{"altitude": 100, "speed": 12, "battery": 95}'
```

---

## 5. Module Purposes & Key Comments

### `app.py`
- **Purpose:** Main backend server. Hosts the dashboard, handles telemetry (via MQTT or direct POST), emits real-time updates to the frontend.
- **Key Comments:**
  - "Main backend server for the UAV Telemetry Dashboard"
  - "Hosts the web dashboard"
  - "Handles telemetry data (via MQTT or direct POST)"
  - "Emits real-time updates to frontend via Socket.IO"
  - "Accepts telemetry data via POST for demo/testing without MQTT broker. Emits telemetry and alert events to frontend via Socket.IO."
  - "Setup MQTT client and handlers (runs in background thread)"

### `mqtt_handler.py`
- **Purpose:** Manages the MQTT connection, subscribes to telemetry, forwards data and alerts to the backend, and handles anomaly detection and logging.
- **Key Comments:**
  - "This module manages the MQTT connection for the UAV Telemetry Dashboard backend."
  - "Connects to the MQTT broker"
  - "Subscribes to telemetry topic"
  - "Forwards telemetry and alerts to the Flask-SocketIO server"
  - "Handles anomaly detection and logging"
  - "Callback for when the client receives a CONNACK response from the MQTT broker. Subscribes to the telemetry topic on successful connection."
  - "Callback for when the client disconnects from the broker. Logs the disconnection and attempts to reconnect if unexpected."
  - "Callback for when a PUBLISH message is received from the broker. Parses telemetry, emits to SocketIO, and checks for anomalies."
  - "Runs the MQTT network loop forever in a background thread. Handles incoming messages and maintains connection."
  - "Start the MQTT client loop in a daemon thread"

### `test_mqtt_publish.py`
- **Purpose:** Dummy telemetry publisher for testing/demo, can send data via MQTT or direct POST.
- **Usage:** See above commands.

### `templates/index.html`
- **Purpose:** Frontend dashboard, connects via Socket.IO, displays real-time charts, analytics, and alerts.

---

## 6. Troubleshooting
- **No data on dashboard?**
  - Ensure `python flight_dashboard-main/app.py` is running and the dashboard is open in your browser.
  - Run the dummy script in a separate terminal using the full path.
  - Refresh the dashboard page if needed.
  - Check both terminal windows for errors or warnings.

---

## 7. Updating to GitHub

```sh
git add .
git commit -m "Update project and usage docs for explicit path commands"
git push
```

---

For more details, see the main README or the code comments in each file. 