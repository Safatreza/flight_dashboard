"""
MQTT Handler Module
- Connects to MQTT broker
- Subscribes to 'uav/telemetry'
- Emits telemetry and alert events via Flask-SocketIO
- Handles anomaly detection
- Advanced error handling and logging
"""
import paho.mqtt.client as mqtt
import json
import threading
import logging

def setup_mqtt(socketio, broker_host="localhost", broker_port=1883, topic="uav/telemetry"):
    """
    Initializes and starts the MQTT client in a background thread.
    Emits telemetry and alert events to SocketIO.
    """
    logger = logging.getLogger("mqtt_handler")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    if not logger.hasHandlers():
        logger.addHandler(handler)

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info(f"Connected to MQTT broker at {broker_host}:{broker_port}")
            try:
                client.subscribe(topic)
                logger.info(f"Subscribed to topic '{topic}'")
            except Exception as e:
                logger.error(f"Failed to subscribe to topic '{topic}': {e}")
        else:
            logger.error(f"Failed to connect to MQTT broker (rc={rc})")

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            logger.warning("Unexpected disconnection from MQTT broker. Trying to reconnect...")
        else:
            logger.info("Disconnected from MQTT broker.")

    def on_message(client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            logger.info(f"Received MQTT message: {payload}")
            socketio.emit('telemetry', payload)
            # Anomaly detection
            alerts = []
            battery = payload.get('battery')
            altitude = payload.get('altitude')
            if battery is not None and battery < 20:
                alerts.append(f"Warning: Low battery ({battery}%)")
            if altitude is not None and altitude < 5:
                alerts.append(f"Warning: Low altitude ({altitude} meters)")
            for alert in alerts:
                socketio.emit('alert', {'message': alert})
                logger.warning(f"Anomaly detected: {alert}")
        except json.JSONDecodeError:
            logger.error(f"Failed to decode MQTT message: {msg.payload}")
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_message = on_message
    try:
        mqtt_client.connect(broker_host, broker_port, 60)
    except Exception as e:
        logger.critical(f"Failed to connect to MQTT broker at {broker_host}:{broker_port}: {e}")
        return

    def mqtt_loop():
        try:
            mqtt_client.loop_forever()
        except Exception as e:
            logger.critical(f"MQTT client loop stopped unexpectedly: {e}")

    mqtt_thread = threading.Thread(target=mqtt_loop)
    mqtt_thread.daemon = True
    mqtt_thread.start() 