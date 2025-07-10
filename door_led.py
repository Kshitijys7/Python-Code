import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False)
sleepTime = 5
ledPin = 11

def ledSetup():
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setwarnings(False)
    
#GPIO.setwarnings(False) # Ignore warning for now

#GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
def ledON():
    GPIO.output(ledPin, True)
    sleep(sleepTime)
    GPIO.cleanup()

def call_led():
    GPIO.setwarnings(False)
    ledSetup()
    ledON()
