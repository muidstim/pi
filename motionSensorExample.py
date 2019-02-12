from gpiozero import MotionSensor, Buzzer, LED
import time

pir = MotionSensor(23)
bz = Buzzer(24)
led = LED(18)
print("Waiting for PIR to settle")
pir.wait_for_no_motion()

while True:
    led.off()
    print("Ready")
    pir.wait_for_motion()
    led.on()
    print("Motion detected!")
    bz.beep(0.5, 0.25, 8)
    time.sleep(3)
