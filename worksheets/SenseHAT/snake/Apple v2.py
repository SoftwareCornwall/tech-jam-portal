from sense_hat import SenseHat
import random
sense = SenseHat()
from time import sleep
apple_loc = [0,0]
RED = (100,0,0)
b=(0,0,0)

apple_loc=[0,0]

def apple_place():
    apple_x = random.randint(0,7)
    apple_y = random.randint(0,7)
    return apple_x, apple_y
#pick random spot
    
def apple_draw():
    global apple_loc
    sense.set_pixel(apple_loc[0] ,apple_loc[1] , b )
    apple_x , apple_y = apple_place()
    x = int(apple_x)
    y = int(apple_y)
    apple_loc[0] = x
    apple_loc[1] = y
    sense.set_pixel(apple_x,apple_y,RED)
#places apple when up is pressed

def pushed_up(event):
    apple_draw()

while True:
    sense.stick.direction_up = pushed_up
    
    #if event.action == "pressed":
     #   apple_x, apple_y = apple_place()
      #  apple_loc = [apple_x , apple_y]
       # sense.set_pixels(apple_loc , RED)
    
    
    
    
    