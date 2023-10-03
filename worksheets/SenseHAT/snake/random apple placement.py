from sense_hat import SenseHat
import random
sense = SenseHat()
from time import sleep

RED = (100,0,0)
b=(0,0,0)
#colour for apples

matrix = [[b for column in range(8)] for row in range(8)]
def flatten(matrix):
    flattened =[pixel for row in matrix for pixel in row]
    return flattened
#flattens the matrix

def apple(matrix):
    num_x = random.randint(0,7)
    num_y = random.randint(0,7)
    matrix[num_x][num_y] = RED
    return matrix
#places apples randomly


while True:
    matrix = apple(matrix)
    sense.set_pixels(flatten(matrix))
    sleep(1)
#the game running
    
    
