import Adafruit_DHT

while True:
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  print ("Temperature:", temperature)
  print ("Humidity:", humidity)
