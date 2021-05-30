import time #Library for time-related tasks
import RPi.GPIO as GPIO #Library for the GPIO Pins
import lcd_i2c #required to use the LCD, must also have lcd_i2c.py file in the same directory as your script

#Setup and initialization functions of the LCD
def printLCD(string1, string2):
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
pin.start(0) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
time.sleep(1) #sleep for a second to ensure signal is initialized properly

#Determining string inputs for LCD, the first string is static, in the second string we use variables as inputs
inputstring1 = "Welcome" #The string we send to the LCD
inputstring2 = "Goodbye" #The string we send to the LCD

print("Begin") #informs user the main function of the program is beginning

try:
    printLCD(inputstring1,"") #prints to LCD
    time.sleep(2) #sleep for 2 seconds
    
    #Main portion of program
    pin.ChangeDutyCycle(50) #changes the duty cycle to 50%
    time.sleep(5) #sleeps for 5 seconds
    pin.stop() #stops the pin initialization

    printLCD(inputstring2,"") #prints to LCD
    time.sleep(2) #sleep for 2 seconds

except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass

lcd_i2c.cleanup() #LCD cleanup
GPIO.cleanup() #cleans up all of the GPIO pins used within the script

print("Done") #informs the user the program is finished running