# Microbit code for Rover

from microbit import *
import radio

# define named variables for the motor pin connections
enable_left_motor = pin13
enable_right_motor = pin2

forwards_right = pin1
backwards_right = pin8

forwards_left = pin14
backwards_left = pin16

# turn on the radio using default channel 7
#radio.config(channel=6)
radio.on()

# define the functions to move the rover
def forwards():
    enable_left_motor.write_analog(1023)      # on
    enable_right_motor.write_analog(800)     # on
    forwards_right.write_digital(1)     # on
    backwards_right.write_digital(0)    # off
    forwards_left.write_digital(1)      # on
    backwards_left.write_digital(0)     # off

def backwards():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(0)
    backwards_right.write_digital(1)
    forwards_left.write_digital(0)
    backwards_left.write_digital(1)

def stop():
    enable_left_motor.write_digital(0)
    enable_right_motor.write_digital(0)
    forwards_right.write_digital(0)
    backwards_right.write_digital(0)
    forwards_left.write_digital(0)
    backwards_left.write_digital(0)

def left():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(1)
    backwards_right.write_digital(0)
    forwards_left.write_digital(0)
    backwards_left.write_digital(1)

def right():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(0)
    backwards_right.write_digital(1)
    forwards_left.write_digital(1)
    backwards_left.write_digital(0)




while True:
    message = radio.receive()
    if message == "F":
        forwards()
        display.show(Image.ARROW_W)
    elif message == "B":
        backwards()
        display.show(Image.ARROW_E)
    elif message == "L":
        left()
        display.show(Image.ARROW_S)
    elif message == "R":
        right()
        display.show(Image.ARROW_N)

    else:
        stop()
        display.show(Image.NO)
    sleep(10)