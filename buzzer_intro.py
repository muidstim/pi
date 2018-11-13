import RPi.GPIO as GPIO

buzzer_pin = 27

def setup():
  GPIO.setmode(GPIO.BCM
  GPIO.setup(buzzer_pin, GPIO.IN)
  GPIO.setup(buzzer_pin, GPIO.OUT)
  
try:
  setup()
finally:
  GPIO.cleanup()
  print("done")
