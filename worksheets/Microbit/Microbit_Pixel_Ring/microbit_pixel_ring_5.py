from microbit import *
import neopixel
from random import randint

ring = neopixel.NeoPixel(pin0, 16)

# initially set the colour values to zero
# the variables need to be defined before use

red = 0
green = 0
blue = 0
off = (0, 0, 0)

def chase(use_this_colour):
    for led_number in range(0, 16):
        ring[led_number] = use_this_colour
        ring[led_number - 2] = off
        ring.show()
        sleep(50)

def random_colour():
    red = randint(0, 75)
    green = randint(0, 75)
    blue = randint(0, 75)
    colour = (red, green, blue)
    return colour

while True:
    chase(random_colour())