import time
import RPi.GPIO as GPIO

print("Setup") #informs user setup has begun

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setup(25, GPIO.OUT) #sets GPIO pin 25 as an output

#PWM Signal Setup
pin = GPIO.PWM(25,50) #set pin 25 as a PWM output, with a frequency of 50 Hz
pin.start(0) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
time.sleep(1) #sleep for a second to ensure signal is initialized properly

print("Begin") #informs user the main function of the program is beginning

#Main portion of program
pin.ChangeDutyCycle(50) #changes the duty cycle to 50%
time.sleep(5) #sleeps for 5 seconds

pin.stop() #stops the pin initialization
GPIO.cleanup() #cleansup all of the GPIO pins used within the script

print("Done") #informs the user the program is finished running