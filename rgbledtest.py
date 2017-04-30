from microbit import *


# WTF??? my pin input and output is reversed.  0 outputs, 1 inputs digital
# and the same for analog: 1023 is low, 1 is high?

x = 1023
while x > 0:
    pin0.write_analog(x)
    sleep(1000)
    x = x - 50
    
pin0.write_analog(1023)
sleep(1000)

x = 1023
while x > 0:
    pin2.write_analog(x)
    pin0.write_analog(x)
    sleep(1000)
    x = x - 50
    
pin2.write_analog(1023)
pin0.write_analog(1023)