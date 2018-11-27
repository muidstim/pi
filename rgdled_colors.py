from picamera import Color

led = RGBLED(12, 20, 16)# or whatever pins you’re using
led.color = Color('#ffffff')# supports HTML color specs
led.color = Color('violet')# or CSS color names
led.color = Color(255, 127, 0)# or 0-255 bytes
led.color = Color(0.0, 0.5, 0.0)# or 0-1 floats
led.color = Color(hue=0, saturation=0.5, lightness=0.5)
