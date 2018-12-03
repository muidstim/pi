import #BLANK#
from #BLANK#

trackPin = 21

def detect():
  while True:
    tracking = GPIO.input(trackPin)
    print(tracking)
    if tracking == GPIO.LOW:
      print("#BLANK# detected")
    else:
      print("... #BLANK# detected")
    sleep(0.1)
    
try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(trackPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  #BLANK#
finally:
  #BLANK#
