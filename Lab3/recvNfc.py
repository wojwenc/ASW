#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import threading
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect_local(client_local, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client_local.subscribe("sensors/nfc")

# The callback for when a PUBLISH message is received from the server.
def on_message_local(client_local, userdata, msg):
    print(str(b'd\n\xd1\xaf'))
    print(str(msg.payload))
    if "bytearray(b'd\\n\\xd1\\xaf')" == str(msg.payload):
        client_local.publish("led/504", 1)
        time.sleep(5)
        client_local.publish("led/504", 0)
    else:
        client_local.publish("led/505", 1)
        time.sleep(5)
        client_local.publish("led/505", 0)
        

client_local = mqtt.Client()
client_local.on_connect = on_connect_local
client_local.on_message = on_message_local
client_local.connect("localhost", 1883, 60)

threading.Thread(target=client_local.loop_forever).start()