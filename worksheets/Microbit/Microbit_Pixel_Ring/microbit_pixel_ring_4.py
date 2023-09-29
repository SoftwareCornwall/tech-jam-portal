from microbit import *
import neopixel

ring = neopixel.NeoPixel(pin0, 5)

# set some variables for colours
red = (75, 0, 0)
green = (0, 75, 0)
blue = (0, 0, 75)
off = (0, 0, 0)

# define (def) a function and give it a clear, simple name.
# The bracket after does not have
# to have anything in it if it is not required.
# Here the colours are sent from the call at the bottom
# and renamed use_this_colour.

def chase(use_this_colour):
    for led_number in range(0, 5):
        ring[led_number] = use_this_colour
        ring[led_number - 2] = off
        ring.show()
        sleep(50)

while True:
    chase(red)
    chase(green)
    chase(blue)