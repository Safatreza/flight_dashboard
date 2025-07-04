# UAV Telemetry Dashboard — Quick Start (Simplified Dummy Mode)

Get started in just a few steps!

---

## 1. Start Dummy Data and Backend

From your project root (`D:/Flight_Dashboard/flight_dashboard-main`):

**Open two terminals:**

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

In a third terminal, run:
```sh
python -m http.server 8050 --directory flight_dashboard-main/static_dashboard
```

Then open your browser and go to:
```
http://localhost:8050/index.html
```

You should now see live-updating charts and alerts as dummy data streams in!

---

## Troubleshooting
- **404 Error?**
  - Make sure you ran the http.server command above from the project root.
  - Visit `http://localhost:8050/index.html` in your browser.
  - Confirm `index.html` exists in `flight_dashboard-main/static_dashboard/`.
- **No Data?**
  - Ensure both the backend and dummy publisher are running.

---

For more details, see the main README or code comments in each file. 