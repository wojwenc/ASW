#!/usr/bin/env python3.6
import gpio
import logging
print( "Test BTN\n")
BTN = 488
LED = 504
gpio.log.setLevel(logging.INFO)
gpio.setup(LED , gpio.OUT)
gpio.setup(BTN, gpio.IN)

# read btn value and set apropriate led state
prev = gpio.read(BTN)
gpio.set(LED, prev)
while(True):
    value = gpio.read(BTN)
    if value != prev: 
        print(value)
        gpio.set(LED, value) # if changed change led status based on btn value
    prev = value


    