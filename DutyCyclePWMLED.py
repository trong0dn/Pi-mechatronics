import time #Library for time-related tasks
import RPi.GPIO as GPIO #Library for the GPIO Pins
import lcd_i2c #required to use the LCD, must also have lcd_i2c.py file in the same directory as your script

#Setup and initialization functions of the LCD
def printLCD(string1, string2=""):
    lcd_i2c.printer(string1, string2)
def setup():
    lcd_i2c.lcd_init()

setup() #calls setup function of the LCD 
print("Setup") #informs user setup has begun

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setup(25, GPIO.OUT) #sets GPIO pin 25 as an output

#PWM Signal Setup
pin = GPIO.PWM(25,50) #set pin 25 as a PWM output, with a frequency of 50 Hz

print("Begin") #informs user the main function of the program is beginning

try:

    #Main portion of program
    for i in range (0,120,20): #iterates from 0 to 120 (exclusive) in increments of 20%
        pin.start(i) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
        printLCD(i) #prints the current duty cycle for each increment LCD
        print("Current duty cycle:", i) #informs the user of the current duty cycle for each increment using the LCD
        time.sleep(1) #sleep for a second to ensure signal is initialized properly
    pin.stop() #stops the pin initialization

except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass

GPIO.cleanup() #cleans up all of the GPIO pins used within the script
lcd_i2c.cleanup() #LCD cleanup

print("Done") #informs the user the program is finished running