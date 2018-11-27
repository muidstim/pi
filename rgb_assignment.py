# complete this code, you must import the correct libraries and finish each function
from gpiozero import __________
from time import __________

def blue():
  # Slowly increase the intensity from dark blue to bright blue
  
def red():
  # Slowly increase the intensity from dark red to bright red
    
def green():
  # Slowly increase the intensity from dark green to bright green

#DO NOT use the color codes, simply combine the R, G, B
def magenta():
  #set the color to magenta
  
#DO NOT use the color codes, simply combine the R, G, B
def cyan():
  #set the color to cyan


try:
  blue()
  sleep(1)
  red()
  sleep(1)
  green()
  sleep(1)
  magenta()
  sleep(1)
  cyan()
  sleep(1)
finally:
  led.off()
  print("done")
