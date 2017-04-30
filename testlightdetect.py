# Example use of sensor with microbit
# This particular test used a Sunfounder photoresistor, 
# though any photoresistor should work equally well.

# When more light is applied, the value returned is less
# When less light is applied, the value returned is greater

# Worked well, readings were consistent within a range
# When using, be sure to buff out minor changes in room lighting.

from microbit import *

while True:
    myreturn = pin0.read_analog()
    display.scroll(str(myreturn))
    sleep(2000)