def setup():
  print("Setting Up Touch Sensor and LED")
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  
  
try:
  print("Raspberry Pi Touch Sensor Sample Program")
  setup()
  print("Setup Complete")
  loop()
finally:
  print("done")
