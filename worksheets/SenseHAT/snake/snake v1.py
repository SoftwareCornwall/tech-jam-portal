from sense_hat import SenseHat
import random
sense = SenseHat()
from time import sleep
RED = (100,0,0)
r = 100
g = 100
b = 100
white = (100,100,100)
#off = (0,0,0)
snake_body = [[0,4]]
apple_loc=[0,0]
snake_y = 4
snake_x = 0
score = 0
game = True
def get_longer():
    current_tail = snake_body[len(snake_body)-1]
    new_tail = current_tail[1]+1
    if new_tail >= 8:
        new_tail = new_tail - 2
    new_tail = [current_tail[0], new_tail]
    snake_body.append(new_tail)


def apple_place():
    apple_x = random.randint(0,7)
    apple_y = random.randint(0,7)
    return apple_x, apple_y
#pick random spot
    
def apple_draw():
    global apple_loc
    sense.set_pixel(apple_loc[0] ,apple_loc[1] , off )
    apple_x , apple_y = apple_place()
    x = int(apple_x)
    y = int(apple_y)
    apple_loc[0] = x
    apple_loc[1] = y
    sense.set_pixel(apple_x,apple_y,RED)
#places apple
    
def body_move():
    global snake_body
    for i in range(len(snake_body)-1,0,-1):
        snake_body[i] = snake_body[i-1]
    
    


def draw_snake():
    sense.set_pixel(apple_loc[0], apple_loc[1],RED)
    sense.set_pixel(snake_x,snake_y,white)
    for i in range(len(snake_body)-1,0,-1):
        sense.set_pixel(snake_body[i][0] , snake_body[i][1] , white)
#places snake on LEDS
    
def move_up(event):
    global snake_y
    if snake_y == 0 and event.action == "pressed":
        body_move()
        snake_y=7
    elif event.action == "pressed":
        body_move()
        snake_y -= 1
    snake_body[0] = [snake_x,snake_y]
#move up if snake at top teleport to bottom
        
def move_down(event):
    global snake_y
    if snake_y == 7 and event.action == "pressed":
        body_move()
        snake_y=0
    elif event.action == 'pressed':
        body_move()
        snake_y += 1
    snake_body[0] = [snake_x,snake_y]
#snake move down if at bottom teleport to top
        
        
def move_right(event):
    global snake_x
    if snake_x == 7 and event.action =="pressed":
        body_move()
        snake_x=0
    elif event.action == 'pressed':
        body_move()
        snake_x += 1
    snake_body[0] = [snake_x, snake_y]
#snake move right if snake at right edge teleport to left
        
def move_left(event):
    global snake_x
    if snake_x==0 and event.action == "pressed":
        body_move()
        snake_x=7
    elif event.action == 'pressed':
        body_move()
        snake_x -= 1
        snake_body[0] = [snake_x , snake_y]
#snake move left if snake at left edge teleport to right



apple_draw()
while game ==True:
    sense.stick.direction_down = move_down
    draw_snake()
    sleep(0.25)
    sense.clear(0,0,0)
    
    sense.stick.direction_up = move_up
    draw_snake()
    sleep(0.25)
    sense.clear(0,0,0)
    
    sense.stick.direction_right = move_right
    draw_snake()
    sleep(0.25)
    sense.clear(0,0,0)
    
    sense.stick.direction_left = move_left
    draw_snake()
    sleep(0.25)
    sense.clear(0,0,0)
    
    if snake_x == apple_loc[0] and snake_y == apple_loc[1]:
        apple_draw()
        score+=1
        print("score: " ,score)
        get_longer()
    if len(snake_body) >= 2:  
        for item in range(len(snake_body)-1):
            if snake_x== snake_body[item+1][0] and snake_y == snake_body[item+1][1]:
                print("game over")
                print("Your score = ", score)
                game = False
        
    