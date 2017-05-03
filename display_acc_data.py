from microbit import *


def display_acc_data():
    my_send = accelerometer.get_values()               
    display.scroll("x")
    display.scroll(str(my_send[0]))
    display.scroll("y")
    display.scroll(str(mysend[1]))
    display.scroll("z")
    display.scroll(str(mysend[2]))
    sleep(800)
    
while True:
  if button_a.was_pressed():
    display_acc_data()
