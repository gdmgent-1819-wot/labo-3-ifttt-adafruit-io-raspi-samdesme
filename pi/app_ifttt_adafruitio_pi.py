# Import standard python modules.
import random
import sys
import time
import pygame
import threading
import timeit
import datetime

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client, Data

from threading import Thread
from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from random import randint
from time import sleep
from signal import pause

# Set to your Adafruit IO key & username.
ADAFRUIT_IO_KEY = 'cf3df94c4c2d42159f32b14da19554d2'
ADAFRUIT_IO_USERNAME = 'samdesme'

# Feeds 
group_feed_btn = 'btnpressed'
group_feed_time = 'Reactie-tijd'

sense = SenseHat()
start = time.time()

def sparkles() :
    while True:
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.01)
        
def playSound() :
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("analog.wav")
        pygame.mixer.music.play()
    
def connected(client):
    
    # Subscribe to feed where you want to detect changes from
    client.subscribe(group_feed_btn)
    client.subscribe(group_feed_time) 
    print('Listening for changes on ', group_feed_btn)


def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    if payload == "button_pressed":
        
        # define globale variable
        global start
        
        # get timestamp when button is pressed
        print ("Button was pressed!")
        start = time.time()
        
        # start matrix & play sound
        Thread(target = sparkles).start()
        Thread(target = playSound).start()
        
        # return value of variable
        return start

def joystickMiddle(event):
    if event.action == ACTION_RELEASED:
        
        # new timestamp
        end = time.time()
        
        # calculate reaction time
        timeVal = end - start
        
        # publish value to feed
        client.publish(group_feed_time, timeVal)
        client.disconnect()

sense.stick.direction_middle = joystickMiddle

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Loop to check for changes
client.loop_blocking()

