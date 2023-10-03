# Microbit code for Remote Control

from microbit import *
import radio

radio.on()

while True:
    if accelerometer.is_gesture("down"):
        radio.send("F")
        display.show(Image.ARROW_N)
    elif accelerometer.is_gesture("down"):
        radio.send("F")
        display.show(Image.ARROW_N)
    elif accelerometer.is_gesture("left"):
        radio.send("L")
        display.show(Image.ARROW_W)
    elif accelerometer.is_gesture("right"):
        radio.send("R")
        display.show(Image.ARROW_E)

    else:
        radio.send("S")
        display.show(Image.PACMAN)
    sleep(10)