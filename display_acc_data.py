from microbit import *


radio.on()

def display_acc_data():
    my_send = accelerometer.get_values()               
    display.scroll("x")
    display.scroll(my_send[0])
    display.scroll("y")
    display.scroll(mysend[1])
    display.scroll("z")
    display.scroll(mysend[2])
    sleep(800)
    
while True:
  if button_a.was_pressed():
    display_acc_data()
