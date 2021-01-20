#!/usr/bin/env python3.6
from py532lib.mifare import *
from py532lib.frame import *
from py532lib.constants import *
import time
import paho.mqtt.client as mqtt
import threading

client_local = mqtt.Client()
client_local.connect("192.168.51.231", 1883, 60)

card = Mifare()
card.i2c_channel=9
card.reset_i2c()
# Configure the PN532 for the number of retries attempted
# during the InListPassiveTarget operation (set to
# MIFARE_SAFE_RETRIES=5 for a safe one-time check
card.set_max_retries(MIFARE_SAFE_RETRIES)
#Send a SAMCONFIGURATION (Secure Access Module) command to the PN532 
card.SAMconfigure()
while(True):
    uuid = card.scan_field()
    if uuid:
        print(uuid)
        client_local.publish("sensors/nfc", str(uuid))
        address = card.mifare_address(0,1)
        card.mifare_auth_a(address,MIFARE_FACTORY_KEY)
        data = card.mifare_read(address)
        print(data)
        card.in_deselect() # In case you want to authorize a different sector.
    elif(int(time.time())%5==0):
        print("Not find any new tag, wait for next 5 sec...")
        sleep(1)