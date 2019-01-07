import RPi.GPIO as #BLANK#
import #BLANK#

#BLANK# - set the pin

def setup():
  print("Setting Up Touch Sensor and LED on pin", TouchPin)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  
def detectTouch():
  while True:
    time.sleep(0.2)
    
    if GPIO.input(#BLANK#) == GPIO.LOW:
      print ('...led off')
    else:
      print ('led on...')
      
try:
  print("Raspberry Pi Touch Sensor Sample Program")
  #BLANK#  
  print("Setup Complete")
  detectTouch()
finally:
  #BLANK#
  print("done")
