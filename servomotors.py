"""
https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/

This project uses Python scripts run on a Raspberry Pi microcontroller to send GPIO PWM 
outputs to a servo motor to set its angle. 

A servo motor is a type of DC motor that, upon receiving a signal of a certain frequency, 
can rotate itself to any angle from 0-180 degrees. Its 90 degree position is generally 
referred to as 'neutral' position, because it can rotate equally in either direction 
from that point.

The way a servo motor reads the information it's being sent is by using an electrical signal 
called PWM.

PWM stands for "Pulse Width Modulation". 

That just means sending ON electrical signals for a certain amount of time, followed by 
an OFF period, repeated hundreds of times a second. The amount of time the signal is on 
sets the angle the servo motor will rotate to. In most servos, the expected frequency is 
50Hz, or 3000 cycles per minute. Servos will set to 0 degrees if given a signal of .5 ms, 
90 when given 1.5 ms, and 180 when given 2.5ms pulses. This translates to about 2.5-12.5% 
duty in a 50Hz PWM cycle.

"""
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Now we need an output to send our PWM signal on, so write

GPIO.setup(03, GPIO.OUT)
#Now setup PWM on pin #3 at 50Hz
pwm=GPIO.PWM(03, 50) 

#Then start it with 0 duty cycle so it doesn't set any angles on startup

pwm.start(0)

"""
Now, to set the angle of the servo, we need to send a specific signal to it. 
This can differ from servo to servo, as normally it's from 2.5-12.5%, and on 
the ones I'm using it's 2-12%. Regardless, it will be a 10% window, so to 
calculate the duty cycle for your desired angle, divide by 18, then add the 
lowest available value, in this case 2.

So, for 90 degrees, divide by 18, which is 5, then add 2, and you get 7. 
So on this servo 7% duty is 90 degrees.

As you can see, this math is not very friendly and would be tedious to do 
every time you wanted to set an angle, so in order to simplify that we're 
going to write a function in Python that does the math automatically then sets the angle.

So, first define a function. You can name it whatever you like.
"""

def SetAngle(angle):
	duty = angle / 18 + 2 #sets a variable equal to our angle divided by 18 and 2 added like I showed above
	GPIO.output(03, True) #turns on the pin for output
	pwm.ChangeDutyCycle(duty) #changes the duty cycle to match what we calculated
	
	#waits 1 second so the servo has time to make the turn. 
	#Depending on the speed of your servo you might need longer, or you might not need this long
	sleep(1) 
	
	GPIO.output(03, False) #turns off the pin
	
	pwm.ChangeDutyCycle(0) #changes the duty back to 0 so we aren't continuously sending inputs to the servo


SetAngle(90) 
#to tell the servo to turn to 90 degrees.

pwm.stop()
GPIO.cleanup()


"""
Note: you may receive an error that says the selected GPIO channels are already in use. 
This won't affect your project, and you can make the warnings stop appearing by writing 

GPIO.setwarnings(False)

"""
