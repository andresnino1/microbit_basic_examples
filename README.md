# Micro Bit Basic Examples

Repositories to house tests conducted with the microbit.

If you are visiting this repository, be bold! Take a look at the following link:
* https://microbit-micropython.readthedocs.io/en/latest/

Of the coding documentation I have read in my (mere) 7 months of serious programming, this documentation is by far some of the easiest to follow.... because the libraries leave almost no room for error!  What I mean to say is, you can accomplish in one line of code (or one sentence of thought, if you will) what might be accomplished in Python on the Raspberry Pi in multiple lines.  Consider the Raspberry Pi GPIO Access:
```
import RPi.gpio As GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,True)
```

Compare that with the alternative:

```
from microbit import *

pin0.write_digital(1)
```

You can't get much simpler!  Just import everything from microbit (using an asterisk) and you have what you need.  Then just identify the pin you want to write or read from.

*Note: I will say, one caveat you may experience with the microbit is an inversion of the pin values: for me, 0 = "on" and 1 = "off".  This is not typical behavior.*
