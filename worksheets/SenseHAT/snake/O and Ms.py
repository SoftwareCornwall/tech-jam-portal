from time import sleep
from sense_hat import SenseHat
import pygame
from pygame.locals import*
import copy

sense = SenseHat()

pygame.init()
pygame.display.set_mode((500, 500))

x=0
y=0

picture = [[0,0,0]] *64

draw_colours=[[0,0,0] , [248,248,248],[248,0,0], [0,248,0], [0,0,248], [248,248,0], [0,248,248],[248,0,248]]



def draw_picture_and_cursor(picture):

    cursor_colour = [248,248,248]
    tmp_pic = copy.deepcopy(picture)
    tmp_pic[(y*8)+x] = cursor_colour
    sense.set_pixels(tmp_pic)

def get_next_colour():
    current_colour = picture[(y*8)+x]
    current_index = draw_colours.index(current_colour)
    new_index = current_index + 1
    if new_index >=len(draw_colours):
        new_index =0
    new_colour = draw_colours[new_index]
    return new_colour



while True:
    draw_picture_and_cursor(picture)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x = x + 1
            if event.key == K_LEFT:
                x = x - 1
            if event.key == K_UP:
                y = y - 1
            if event.key == K_DOWN:
                y = y + 1
            
            
            
            
            if event.key ==K_1:
                picture[(y*8)+x] = draw_colours[0]
            if event.key ==K_2:
                picture[(y*8)+x] = draw_colours[1]
            if event.key ==K_3:
                picture[(y*8)+x] = draw_colours[2]
            if event.key ==K_4:
                picture[(y*8)+x] = draw_colours[3]
            if event.key ==K_5:
                picture[(y*8)+x] = draw_colours[4]
            if event.key ==K_6:
                picture[(y*8)+x] = draw_colours[5]
            if event.key ==K_7:
                picture[(y*8)+x] = draw_colours[6]
            if event.key ==K_8:
                picture[(y*8)+x] = draw_colours[7]
            
            
            
            if event.key == K_SPACE:
                picture[(y*8)+x] = get_next_colour()
    