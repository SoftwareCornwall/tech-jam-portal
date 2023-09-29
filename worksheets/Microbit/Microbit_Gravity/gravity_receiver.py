from microbit import *
from math import sqrt
import random
import radio

radio.config(channel=7)
radio.on()
display.scroll("Go")

while True:
    message = radio.receive()
    if message:
        message = (int(message)/1000)
        print((message,))
    sleep(200)