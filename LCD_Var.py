import time
import lcd_i2c #required to use the LCD, must also have lcd_i2c.py file in the same directory as your script

#Setup and initialization functions of the LCD
def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)
def setup():
    lcd_i2c.lcd_init()

setup() #calls setup function of the LCD

stingvar = "Station" #Defining string variable
numvar = 1 #defining integer variable

#Determining string inputs for LCD, the first string is static, in the second string we use variables as inputs
inputstring1 = "Hello, I am at" #The string we send to the first line of the LCD
inputstring2 = "%s %d." % (stingvar,numvar) #The string we send to the second line of the LCD

try:
    printLCD(inputstring1,inputstring2) #prints to LCD
    time.sleep(5)#sleep for 5 seconds

except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass

lcd_i2c.cleanup()#LCD cleanup