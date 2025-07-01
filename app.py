"""
UAV Telemetry Flask Backend
- Serves a real-time dashboard
- Connects to MQTT broker and relays telemetry via WebSocket
- Detects anomalies and emits alerts
"""
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from mqtt_handler import setup_mqtt

# Initialize Flask app and SocketIO (eventlet async mode recommended for production)
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    """Serve the main dashboard page."""
    return render_template("index.html")

@app.route("/_dummy_telemetry", methods=["POST"])
def dummy_telemetry():
    """Accepts telemetry data via POST for demo/testing without MQTT broker."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400
    # Emit to WebSocket clients as if it came from MQTT
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

# Setup MQTT client and handlers
setup_mqtt(socketio)

if __name__ == "__main__":
    # Run the Flask-SocketIO server
    socketio.run(app, host="0.0.0.0", port=5000)
