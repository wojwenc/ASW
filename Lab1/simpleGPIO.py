#!/usr/bin/env python3.6
import time
import gpio
print( "Test LED@PWM0\n")
LED = 505
gpio.setup(LED , gpio.OUT)
while(True):
    gpio.set(LED , 1)
    time.sleep(0.5)
    gpio.set(LED, 0)
    time.sleep(0.5)
