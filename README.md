# Micro Bit Basic Examples

Repositories to house tests conducted with the microbit.

**CAUTION** Before you read the code in this repository, you should know something strange has occurred on my microbit.  It would seem that to set my pin to high (run electricity through a pin) I need to set my pin to 0.  This is not typical behavior and it contradicts the documentation https://microbit-micropython.readthedocs.io/en/latest/pin.html.  It might be the result of the external sensors I am using.  My code reflects this phenomenon.

### If you're interested, read the docs!

Seriously. If you are visiting this repository, be bold! Take a look at the following link:
* https://microbit-micropython.readthedocs.io/en/latest/

Coding documentation is something I found deplorable as a newcomer. 7 times out of 10 the documentation you are viewing is written with a highly technical vocabulary, abstract concepts, and a lack of concrete examples.  

This is not the case with Microbit or MicroPython. Of the coding documentation I have read in my (mere) 7 months of serious programming, this documentation is by far some of the easiest to follow to get stuff done quickly.... because the libraries leave almost no room for error!  What I mean to say is, you can accomplish in one line of code (or one sentence of thought, if you will) what might be accomplished in Python on the Raspberry Pi in multiple lines.  Consider the Raspberry Pi GPIO Access:
```
import RPi.gpio As GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)
GPIO.output(23,True)
```

Compare that with the microbit:

```
from microbit import *

pin0.write_digital(1)
```

You can't get much simpler!  Just import everything from microbit (using an asterisk) and you have what you need.  Then just identify the pin you want to write or read from.

Now, any time you import a library with asterisk it can make your code a little less readable, but the alternative is just as easy to implement (and you should consider using this style if you are new to programming, it will help with your memory for libraries):
```
import microbit

microbit.MicroBitDigitalPin.pin0.write_digital(1)
```
Granted its lengthier, but makes sense just by looking at it right?  If you are wondering where I learned to use MicroBitDigitalPin, I learned from the following link:

https://microbit-micropython.readthedocs.io/en/latest/pin.html

Feel free to browse my code or contribute your examples! Any form of participation is welcome.
