"""
https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/

This project uses Python scripts run on a Raspberry Pi microcontroller to send GPIO PWM outputs to a servo motor to set its angle. If all that sounds confusing, don't worry, I'm about to explain it.

A servo motor is a type of DC motor that, upon receiving a signal of a certain frequency, can rotate itself to any angle from 0-180 degrees. Its 90 degree position is generally referred to as 'neutral' position, because it can rotate equally in either direction from that point.

The way a servo motor reads the information it's being sent is by using an electrical signal called PWM. PWM stands for "Pulse Width Modulation". That just means sending ON electrical signals for a certain amount of time, followed by an OFF period, repeated hundreds of times a second. The amount of time the signal is on sets the angle the servo motor will rotate to. In most servos, the expected frequency is 50Hz, or 3000 cycles per minute. Servos will set to 0 degrees if given a signal of .5 ms, 90 when given 1.5 ms, and 180 when given 2.5ms pulses. This translates to about 2.5-12.5% duty in a 50Hz PWM cycle.

First, we need to open a program on the Pi to write our code. We're going to use IDLE 2, so go to the top left of your desktop, click Menu, click Programming, and click Python 2(IDLE). You should see a blank text editor with an untitled document. You should not see a console with a shell prompt (ie. '>>>"). IF you do, click File, then New.

The first thing we need to do is import the GPIO module. So, on the first line, type exactly, CaSe sensitive,
*****************************************************************************************
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
Now, to set the angle of the servo, we need to send a specific signal to it. This can differ from servo to servo, as normally it's from 2.5-12.5%, and on the ones I'm using it's 2-12%. Regardless, it will be a 10% window, so to calculate the duty cycle for your desired angle, divide by 18, then add the lowest available value, in this case 2.

So, for 90 degrees, divide by 18, which is 5, then add 2, and you get 7. So on this servo 7% duty is 90 degrees.

As you can see, this math is not very friendly and would be tedious to do every time you wanted to set an angle, so in order to simplify that we're going to write a function in Python that does the math automatically then sets the angle.

So, first define a function. You can name it whatever you like.
"""

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

"""
Now that probably looks like a lot of confusing code, so let me explain everything I did.

The first line sets up a function called 'SetAngle' that we can call later in the code and give our input as an angle.
The second line (which needs to be indented inside the function) sets a variable equal to our angle divided by 18 and 2 added like I showed above
The third line turns on the pin for output
The fourth line changes the duty cycle to match what we calculated
The fifth line waits 1 second so the servo has time to make the turn. Depending on the speed of your servo you might need longer, or you might not need this long
The sixth line turns off the pin
And the seventh line changes the duty back to 0 so we aren't continuously sending inputs to the servo
Now in your code you can call the function, by writing
"""
SetAngle(90) 
#to tell the servo to turn to 90 degrees.

#So, in your code, call a few angles, and when we run the code we'll see how they run on the servo.

#At the end of your code, make sure to write

pwm.stop()
GPIO.cleanup()
#And that's it! You now have a code that can set your servo to any angle. Press F5, then save to test your code!


"""*Note: you may receive an error that says the selected GPIO channels are already in use. This won't affect your project, and you can make the warnings stop appearing by writing "GPIO.setwarnings(False)" to your code.*"""
