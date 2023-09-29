# Doodle jump for BBC micro:bit
# blog.withcode.uk

# Use A and B to steer

from microbit import *
import random

# force a value to be between a minimum and maximum
def check_bounds(val, min, max):
    if val < min:
        val = min
    if val > max:
        val = max
    return val

# global variables
dx = 50             # doodle x coordinate (0-99)
dy = 50             # doodle y coordinate (0-99)
score = 0           # score
speed_y = 0         # vertical speed
frame = 0           # frame counter

# constants
GAP_BETWEEN_PLATFORMS = 2   # distance between platforms
SCORE_BETWEEN_LEVELS = 10   # number of points you have to score before getting to next level

# initial background image (with platforms)
background = Image("03330:00000:00033:00000:33333")

# time delay for each level of difficulty
levels = [30, 25, 20, 18, 15, 12, 10]
current_level = 0

# keep looping
while True:
    
    # model gravity: increase speed downwards until it reaches terminal velocity
    if speed_y < 5:
        speed_y += 1
    dy += speed_y
        
    # hold button a to move right
    if button_a.is_pressed():
        dx -= 5
    
    # hold butotn b to move left
    if button_b.is_pressed():
        dx += 5
    
    # make sure doodle x and y coordinates are between 0 and 99
    dy = check_bounds(dy, 0, 99)
    dx = check_bounds(dx, 0, 99)
    
    # show the platforms
    display.show(background)
    
    # scale the doodle coordinates down to fit on the micro:bit screen
    dx_scaled = int(5*dx/100)
    dy_scaled = int(5*dy/100)
    
    # increase frame counter
    frame += 1
    
    # scroll down
    if frame % levels[current_level] == 0:
        score += 1
        background = background.shift_down(1)
        
        # advance to next level
        if score % SCORE_BETWEEN_LEVELS == 0:
            current_level += 1
            display.scroll("Level " + str(current_level + 1))
            if current_level >= len(levels):
                current_level = len(levels) - 1
        
        # create new platform
        if score % GAP_BETWEEN_PLATFORMS == 0:
            platform_start = random.randint(0,3)
            platform_end = random.randint(platform_start + 1, 4)
            for x in range(platform_start, platform_end):
                background.set_pixel(x, 0, 3)
    
    # jump if landing on a platform
    if background.get_pixel(dx_scaled, dy_scaled) == 3 and speed_y > 2:
        speed_y = -11
        
    # check if fallen to the floor
    elif dy_scaled == 4:
        display.show(Image.SAD)
        sleep(500)
        display.scroll("Score: " + str(score))
        break
    
    # draw jumping doodle
    display.set_pixel(dx_scaled, dy_scaled, 9)
    
    sleep(20)