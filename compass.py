"""

  THIS IS DIRECTLY FROM MICROPYTHON DOCUMENTATION
  IN MY EXPERIMENTATION, THE COMPASS IS HIGHLY INACCURATE.  SENSITIVE TO TILT
  THIS MAY JUST BE THE WAY THE PROGRAM WAS WRITTEN: THE COMPASS CAN READ X,Y,Z MAGNETIC FIELD STRENGTH

    http://microbit-micropython.readthedocs.io/en/latest/pin.html

    compass.py
    ~~~~~~~~~~

    Creates a compass.

    The user will need to calibrate the compass first. The compass uses the
    built-in clock images to display the position of the needle.

"""
from microbit import *


# Start calibrating
compass.calibrate()

# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
