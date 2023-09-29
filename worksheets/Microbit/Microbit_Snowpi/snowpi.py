from microbit import *
from neopixel import NeoPixel

snowman = NeoPixel(pin2, 12)  # SnowPi connects to Pin 2

#    ¦¦¦¦¦¦¦¦
#    ¦¦¦¦¦¦¦¦
#   ----------
#    11    10
#    ¦  9  ¦
#    -------
#    2  5  8
#   1   4   7
#    0  3  6

blue = (0, 0, 12)
green = (0, 12, 0)
red = (12, 0, 0)
yellow = (12, 12, 0)
off = (0, 0, 0)


tummy = [0, 1, 2, 3, 4, 5, 6, 7, 8]
scarf = [2, 4, 8]
tie = [3, 4, 5]
nose = [9]
eyes = [10, 11]

"""
def light_up(where, colour):
    for led in where:
        snowman[led] = colour
        snowman.show()
        sleep(5)   # pause needed for stability

while True:
    if button_a.was_pressed():
        light_up(tummy, yellow)
        light_up(eyes, blue)
        light_up(scarf, red)
        light_up(nose, green)

    elif button_b.was_pressed():
        light_up(tummy, yellow)
        light_up(eyes, blue)
        light_up(tie, red)
        light_up(nose, green)
    else:
        display.scroll("Press a button")
        snowman.clear()

"""
for light in tummy:
    snowman[light] = yellow
    snowman.show()

for led in scarf:
    snowman[led] = red
    snowman.show()

for glow in eyes:
    snowman[glow] = green
    snowman.show()

for glow in nose:
    snowman[glow] = blue
    snowman.show()

"""
snowman[2] = red
snowman[4] = red
snowman[8] = red

snowman[0] = yellow
snowman[1] = yellow
snowman[3] = yellow
snowman[5] = yellow
snowman[6] = yellow
snowman[7] = yellow


snowman[9] = blue

snowman[10] = green
snowman[11] = green

snowman.show()
"""