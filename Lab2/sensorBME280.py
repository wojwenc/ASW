#!/usr/bin/env python3.6
import time
import paho.mqtt.client as mqtt
import threading

# The callback for when the client receives a CONNACK response from the server.
def on_connect_local(client_local, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client_local.subscribe("gpio/#")

# The callback for when a PUBLISH message is received from the server.
def on_message_local(client_local, userdata, msg):
    value = msg.payload.decode('utf-8')
    if value == '1':
        path = "/sys/bus/iio/devices/iio:device0/in_temp_input"
        with open(path,'r',encoding = 'utf-8') as f:
            client_local.publish("sensors/bme280/temp", str(int(f.read())/1000))

client_local = mqtt.Client()
client_local.on_connect = on_connect_local
client_local.on_message = on_message_local
client_local.connect("192.168.51.231", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

threading.Thread(target=client_local.loop_forever).start()

while(True):
    path = "/sys/bus/iio/devices/iio:device0/in_pressure_input"
    with open(path,'r',encoding = 'utf-8') as f:
        client_local.publish("sensors/bme280/pres", str(f.read()))
    path = "/sys/bus/iio/devices/iio:device0/in_humidityrelative_input"
    with open(path,'r',encoding = 'utf-8') as f:
        client_local.publish("sensors/bme280/hum", str(f.read()))
    time.sleep(5)
