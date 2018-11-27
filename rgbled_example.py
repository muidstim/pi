from gpiozero import RGBLED
from signal import pause

led = RGBLED(17, 18, 4) #red, green, blue gpio pins

try:
  led.red = 1
  print("so red")
  pause()
finally:
  led.off()
