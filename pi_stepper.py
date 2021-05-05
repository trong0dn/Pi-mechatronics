import RPi.GPIO as GPIO
import time
import lcd_i2c

#Setup and initialization functions of the LCD
def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)
def setup():
    lcd_i2c.lcd_init()

def turn():
    for i in range(10):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
    time.sleep(3)

def reverse():
    for i in range(50):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq_reverse[halfstep][pin])
            time.sleep(0.001)
    time.sleep(3)

setup() #calls setup function of the LCD
print("Setup") #informs user setup has begun

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setwarnings(False)

control_pins = [21, 20, 12, 16]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT) #sets GPIO control_pins as an output
    GPIO.output(pin, 0)

# Following matrix should contain the coil energizing sequence for coils A, B, A', and B' 
halfstep_seq = [
  [1,1,0,0], #1
  [0,1,0,0], #2
  [0,1,1,0], #3
  [0,0,1,0], #4
  [0,0,1,1], #5
  [0,0,0,1], #6
  [1,0,0,1], #7
  [1,0,0,0]  #8
]

# Following matrix should contain the coil energizing sequence for coils in reverse
halfstep_seq_reverse = [
  [1,0,0,0], #1
  [1,0,0,1], #2
  [0,0,0,1], #3
  [0,0,1,1], #4
  [0,0,1,0], #5
  [0,1,1,0], #6
  [0,1,0,0], #7
  [1,1,0,0]  #8
]

print("Begin") #informs user the main function of the program is beginning

try:
    turn()
    printLCD("Drink","1")
    turn()
    printLCD("Drink","2")
    turn()
    printLCD("Drink","3")
    turn()
    printLCD("Drink","4")
    turn() 
    printLCD("Your drink","is ready. Enjoy")
    reverse()
except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass

GPIO.cleanup()
lcd_i2c.cleanup() #LCD cleanup
pin.stop() #stops the pin initialization
GPIO.cleanup() #cleans up all of the GPIO pins used within the script

print("Done") #informs the user the program is finished running
