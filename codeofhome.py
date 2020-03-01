import RPi.GPIO as GPIO
import sys
#import Adafruit_IO
from Adafruit_IO import MQTTClient
#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
ledPin = 27
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
ADAFRUIT_IO_KEY = 'Your KEY'
ADAFRUIT_IO_USERNAME = 'USERNAME'
#FEED_ID = 'bulb'
def connected(client):
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format('bulb'))
    client.subscribe('bulb')
    print('Subscribing to Feed {0}'.format('bedlights'))
    client.subscribe('bedlights')
    print('Subscribing to Feed {0}'.format('fan'))
    client.subscribe('fan')
    print('Subscribing to Feed {0}'.format('security'))
    client.subscribe('security')
    print('Subscribing to Feed {0}'.format('app'))
    client.subscribe('app')
    print('Waiting for feed data...')

def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
 if feed_id == 'bulb':
        print('Feed {0} received new value: {1}'.format(feed_id,payload))
        if payload == 'ON':
            print("Hall lights ON")
            GPIO.output(ledPin, 0)
        else:
            print("Hall lights OFF")
            GPIO.output(ledPin, 1)
 elif feed_id == 'bedlights':
        if payload == 'ON':
            print("Bedroom lights on")
            GPIO.output(17, 0)
        else:
            print("Bedroom lights off")
            GPIO.output(17, 1)
 elif feed_id == 'app':
        if payload == 'ON':
            print("All lights on")
            GPIO.output(17, 0)
            GPIO.output(27, 0)
        else:
            print("All lights off")
            GPIO.output(17, 1)
            GPIO.output(27, 1)
 elif feed_id == 'fan':
        if payload == 'ON':
            print(" lights on")
            GPIO.output(22, 0)
        else:
            print("lights off")
            GPIO.output(22, 1)
 elif feed_id == 'security':
        if payload == 'ON':
            print("All lights and security ON")
            GPIO.output(17, 0)
            GPIO.output(27, 0)
            GPIO.output(22, 0)
        else:
            print("All lights and security off")
            GPIO.output(17, 1)
            GPIO.output(27, 1)
            GPIO.output(22, 1)
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_blocking()
