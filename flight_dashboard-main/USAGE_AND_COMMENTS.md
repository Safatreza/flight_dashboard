# UAV Telemetry Dashboard — Usage & Comments

**Note:** The dashboard is now served as a static site using Python's built-in HTTP server. Real-time features (if needed) are still provided by the backend on port 5050.

---

## 1. Setup & Installation

```sh
# Install Python dependencies (from project root or any subdirectory)
pip install -r flight_dashboard-main/requirements.txt
pip install eventlet
```

---

## 2. Serving the Dashboard (Static Mode)

1. **Serve the dashboard with Python's HTTP server:**
   ```sh
   python -m http.server 8050 --directory flight_dashboard-main/static_dashboard
   ```
2. **Open the dashboard in your browser:**
   ```sh
   python -m webbrowser http://localhost:8050/index.html
   # Or manually visit:
   # http://localhost:8050/index.html
   ```

---

## 3. Running in Dummy Mode (No MQTT Broker Required, Real-Time Features)

**Dummy mode** allows you to demo and visualize the dashboard, analytics, and alerting features even if you do not have an MQTT broker installed or running. This is ideal for quick demos, development, or sharing the project with others.

**Steps:**
1. Start the backend server (for real-time data):
   ```sh
   python flight_dashboard-main/app.py
   ```
2. In a new terminal, run the dummy publisher in no-broker mode:
   ```sh
   python flight_dashboard-main/test_mqtt_publish.py --no-mqtt
   ```
3. Open or refresh your browser at:
   [http://localhost:8050/index.html](http://localhost:8050/index.html)
   (The dashboard will connect to the backend at port 5050 for real-time data.)

**What to expect:**
- The dashboard will show live-updating charts for altitude, speed, and battery.
- Analytics tables (min, max, avg) will update as new data arrives.
- If the battery drops below 20% or altitude below 5m, alert popups will appear.
- You do not need any external hardware or MQTT broker for this mode.

**Troubleshooting:**
- If you do not see data, ensure both the backend and dummy script are running, and that you are visiting the correct port (8050 for the dashboard, 5050 for backend API).
- Check both terminal windows for errors or warnings.
- If port 5050 or 8050 is in use, stop any other process using it or change the port in the relevant command or code.

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
- **Purpose:** Main backend server. Hosts the real-time API, handles telemetry (via MQTT or direct POST), emits real-time updates to the frontend.

### `mqtt_handler.py`
- **Purpose:** Manages the MQTT connection, subscribes to telemetry, forwards data and alerts to the backend, and handles anomaly detection and logging.

### `test_mqtt_publish.py`
- **Purpose:** Dummy telemetry publisher for testing/demo, can send data via MQTT or direct POST.

### `static_dashboard/index.html`
- **Purpose:** Frontend dashboard, connects via Socket.IO to the backend, displays real-time charts, analytics, and alerts.

---

## 6. Troubleshooting
- **No data on dashboard?**
  - Ensure the backend is running (`python flight_dashboard-main/app.py`) and the dashboard is open in your browser at [http://localhost:8050/index.html](http://localhost:8050/index.html).
  - Run the dummy script in a separate terminal using the full path.
  - Refresh the dashboard page if needed.
  - Check both terminal windows for errors or warnings.

---

## 7. Updating to GitHub

```sh
git add .
git commit -m "Switch to static dashboard server structure, update usage docs"
git push
```

---

For more details, see the main README or the code comments in each file. 