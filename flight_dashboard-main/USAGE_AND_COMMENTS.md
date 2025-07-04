# UAV Telemetry Dashboard — Universal Quick Start (No Static Directory Needed)

Get your dashboard running from anywhere in your project—no need to be in a specific folder!

---

## 1. Start Dummy Data and Backend

Open two terminals (from anywhere inside your project folder):

**Terminal 1:** Start the backend server:
```sh
python flight_dashboard-main/app.py
```

**Terminal 2:** Start the dummy data publisher:
```sh
python flight_dashboard-main/test_mqtt_publish.py --no-mqtt
```

---

## 2. Open the Dashboard UI

The backend server also serves the dashboard UI. Once the backend is running, simply open your browser and go to:
```
http://localhost:5000/
```

Or, to open it automatically from the terminal (Windows):
```sh
start http://localhost:5000/
```

You should see the dashboard UI with live-updating charts and alerts as dummy data streams in.

---

## Troubleshooting
- **404 or Not Found?**
  - Make sure you started the backend server (`python flight_dashboard-main/app.py`).
  - Visit `http://localhost:5000/` in your browser.
  - Ensure `index.html` exists in the correct templates directory for Flask (usually `flight_dashboard-main/templates/`).
- **No Data?**
  - Ensure both the backend and dummy publisher are running.

---

For more details, see the main README or code comments in each file. 