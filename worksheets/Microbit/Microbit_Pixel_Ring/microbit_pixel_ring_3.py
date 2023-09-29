from microbit import *
import neopixel

ring = neopixel.NeoPixel(pin0, 16)

# set some variables for colours
red = (75, 0, 0)
green = (0, 75, 0)
blue = (0, 0, 75)

# create a list of colours to be read as use_this_colour
colours = [red, green, blue]

while True:
    for use_this_colour in colours:
        for next_led in range(0, 16):
            ring[next_led] = use_this_colour
            ring.show()
            sleep(100)