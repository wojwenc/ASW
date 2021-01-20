#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import threading

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sensors/bme280/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if 'temp' in msg.topic:
        val = int(msg.payload)
        print(val)
        if val > 28:
            client_local.publish("led/504", 1)
        else:
            client_local.publish("led/504", 0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.51.239", 1883, 60)

# The callback for when the client receives a CONNACK response from the server.
def on_connect_local(client_local, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client_local.subscribe("sensors/bme280/#")
    ''
# The callback for when a PUBLISH message is received from the server.
def on_message_local(client_local, userdata, msg):
    if 'temp' in msg.topic:
        val = float(msg.payload)
        print(val)
        if val > 28:
            client_local.publish("led/504", 1)
        else:
            client_local.publish("led/504", 0)

client_local = mqtt.Client()
client_local.on_connect = on_connect_local
client_local.on_message = on_message_local
client_local.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

threading.Thread(target=client_local.loop_forever).start()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
threading.Thread(target=client.loop_forever).start()
