#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import gpio
LED1 = 504
LED2 = 505
gpio.setup(LED1, gpio.OUT)
gpio.setup(LED2, gpio.OUT)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("led/" + str(LED1))
    client.subscribe("led/" + str(LED2))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    led = msg.topic.replace('led/', '')
    gpio.set(int(led), int(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
