# This is the code to be placed on the microbit
from microbit import *

while True:
  sleep(500)
  try:
    bytestring = uart.readline()
    receivedstring = str(bytestring)
    display.scroll(receivedstring)
  except:
    pass
  
