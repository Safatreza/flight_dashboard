"""
UAV Telemetry Flask Backend
- Serves a real-time dashboard
- Connects to MQTT broker and relays telemetry via WebSocket
- Detects anomalies and emits alerts
"""
# Main backend server for the UAV Telemetry Dashboard
# - Hosts the web dashboard
# - Handles telemetry data (via MQTT or direct POST)
# - Emits real-time updates to frontend via Socket.IO

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from mqtt_handler import setup_mqtt

# Initialize Flask app and SocketIO (eventlet async mode recommended for production)
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    """Serve the main dashboard page (frontend UI)."""
    return render_template("index.html")

@app.route("/_dummy_telemetry", methods=["POST"])
def dummy_telemetry():
    """
    Accepts telemetry data via POST for demo/testing without MQTT broker.
    Emits telemetry and alert events to frontend via Socket.IO.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400
    # Emit telemetry to all connected web clients
    socketio.emit('telemetry', data)
    # Anomaly detection (duplicate logic for demo mode)
    alerts = []
    battery = data.get('battery')
    altitude = data.get('altitude')
    if battery is not None and battery < 20:
        alerts.append(f"Warning: Low battery ({battery}%)")
    if altitude is not None and altitude < 5:
        alerts.append(f"Warning: Low altitude ({altitude} meters)")
    for alert in alerts:
        socketio.emit('alert', {'message': alert})
    return jsonify({"status": "ok"})

# Setup MQTT client and handlers (runs in background thread)
setup_mqtt(socketio)

if __name__ == "__main__":
    # Run the Flask-SocketIO server and print the dashboard URL for manual opening
    print("\nDashboard is running! Open http://localhost:5050/ in your browser.\n")
    socketio.run(app, host="0.0.0.0", port=5050)
