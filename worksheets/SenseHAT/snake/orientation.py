
from sense_emu import SenseHat
import random
sense = SenseHat()
sense.clear()
from time import sleep

x=4
y=4



def ball_move (pitch, roll, x,y):
    new_x = x
    new_y = y
    if 1 < pitch <179 and new_x>0:
        new_x-=1
    elif 359 > pitch >181 and new_x<7:
        new_x+=1
    if 1 < roll <179 and new_y>0:
        new_y-=1
    elif 359> roll > 181 and new_y<7:
        new_y+=1
    return new_x, new_y

def get_colour():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    colour = (r,g,b)
    return colour

while True:
    colour = get_colour()
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = ball_move(pitch, roll, x, y)
    sense.set_pixel(x,y,colour)
    sleep(1)
    #print("pitch {0} roll {1}".format(pitch, roll))
