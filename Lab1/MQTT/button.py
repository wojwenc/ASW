#!/usr/bin/env python3.6
import gpio
import logging
import paho.mqtt.client as mqtt
print( "Test BTN\n")
BTN = 488
gpio.log.setLevel(logging.INFO)
gpio.setup(BTN, gpio.IN)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

prev = gpio.read(BTN)
while(True):
    value = gpio.read(BTN)
    if value != prev: 
        print(value)
        client.reconnect()
        client.publish("gpio/488", str(value))
    prev = value


    