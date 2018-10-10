# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client

# Set to your Adafruit IO key & username.
ADAFRUIT_IO_KEY = 'cf3df94c4c2d42159f32b14da19554d2'
ADAFRUIT_IO_USERNAME = 'samdesme'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Feeds 
group_feed_btn = 'btnpressed'
data = aio.data(group_feed_btn)

def connected(client):
    # Subscribe to feed where you want to detect changes from
    client.subscribe(group_feed_btn) 
    print('Listening for changes on ', group_feed_btn)


def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    if payload == "button_pressed":
        print ("Button was pressed!")
        
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

