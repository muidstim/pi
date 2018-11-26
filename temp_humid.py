# you may need to install Adafruit_DHT from the CLI
# sudo pip3 install Adafruit_DHT

import Adafruit_DHT
pin = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(11, pin)
  print ("Temperature:", temperature)
  print ("Humidity:", humidity)
