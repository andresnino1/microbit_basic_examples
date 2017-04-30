#Example demonstrates how to use an rgbled with microbit

# LED
# RGB led used in this project is a Sunfounder product.
# The led uses 3 pins(r,g,b) and a 3volts input
# In this example, pin 0 is blue, pin 1 is green and pin2 is red

from microbit import *


# WTF??? my pin input and output is reversed.  0 outputs, 1 inputs digital
# and the same for analog: 1023 is low, 1 is high?


# Decrement x from 1023 to zero.  This will gradually increase LED brightness
# This loop is a simpe test for the blue color
x = 1023
while x > 0:
    pin0.write_analog(x)
    sleep(1000)
    x = x - 50

# Clear pin 0 (ie, turn out the light)
pin0.write_analog(1023)
sleep(1000)

# Again, decrementing to gradually increase led brightness
# Both red and blue used in tandem to obtain a purple/magenta color
x = 1023
while x > 0:
    pin2.write_analog(x)
    pin0.write_analog(x)
    sleep(1000)
    x = x - 50

# Clear pins 2 and 0
pin2.write_analog(1023)
pin0.write_analog(1023)
