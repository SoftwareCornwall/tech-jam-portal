from microbit import *
import neopixel

ring = neopixel.NeoPixel(pin0, 16)

# set a variable called blue to a colour
blue = (0, 0, 75)

# next_led is another variable that changes from zero
# up to but not including 16 (0 ~ 15)
# The code loops 16 times lighting up the led on
# after another to the colour chosen
# The sleep is just a small pause of 100 milliseconds (1/10th of a second)

for next_led in range(0, 16):
    ring[next_led] = blue
    ring.show()
    sleep(100)