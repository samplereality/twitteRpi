import time
import sys
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# Search terms
TERMS = 'Trump'

# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(0.25)
                        GPIO.output(LED, GPIO.LOW)
                        
# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
while True:
    try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
    
    except (KeyboardInterrupt,SystemExit):
        raise
        GPIO.cleanup()
    except:
        e = sys.exc_info()[0]  #Get exception info (optional)
        print 'ERROR:',e  #Print exception info (optional)
        continue
