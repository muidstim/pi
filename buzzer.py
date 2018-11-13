def buzz(frequency, length):    
  # create the function "buzz" with the pitch and duration)
  if (frequency == 0):
    time.sleep(length)
    return
    
  period = 1.0 / frequency       # the period (sec/cyc) = inverse frequency (cyc/sec)
  delayValue = period / 2        # calcuate the time for half of the wave
  numCycles = int(length * frequency)     # the number of waves to produce
    
  for i in range(numCycles):    
    # start a loop from 0 to the variable "cycles"
    GPIO.output(buzzer_pin, True)   # set pin to high
    time.sleep(delayValue)    # wait with pin high
    GPIO.output(buzzer_pin, False)    # set pin to low
    time.sleep(delayValue)    # wait with pin low
 
 try:
    setup()
    buzz(100,5)
 finally:
    GPIO.cleanup()
    print("done")
