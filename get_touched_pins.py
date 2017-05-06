from microbit import *

def check_pin_touch():
    if pin0.is_touched():
        return"pin2"
    elif pin1.is_touched():
        return "pin1"
    elif pin2.is_touched():
        return "pin2"
    else:
        return "nothing"
    
        
while True:
    mypin = check_pin_touch()
    if mypin != "nothing":
        display.scroll(mypin)
