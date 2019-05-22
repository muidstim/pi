import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pin = 3
GPIO.setup(pin, GPIO.IN)


while True:
    sleep(0.1)
    print(GPIO.input(pin))
