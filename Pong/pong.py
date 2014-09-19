#Pong Game
#Sam Yoder
#9/25/12
#Acknowledgments go to Mehdi and his TA session for ball movement
#Also to Devin for the point_in_rectangle() function allowing for detection
#of ball hitting paddle

from cs1lib import *
from time import sleep
from random import uniform

#constants
HEIGHT = 400
WIDTH = 400
BLOCK_HEIGHT = 80
BLOCK_WIDTH = 20
BLOCK_MOVEMENT = 5
CONTROLS = ["a", "z", "k", "m"]
BALL_RADIUS = 5

def game_over ():
    enable_stroke()
    set_stroke_color (0, 0, 0)
    draw_text ("Game Over. Press Spacebar to play again. Press Q to quit.", 70, 200)
    if is_key_pressed ("q"):
        cs1_quit ()
    elif is_key_pressed (" "):
        start_graphics (pong_game)
        
        
#Alerts program when ball hits a paddle
def ball_hit_paddle(x, y, rx, ry, rw, rh):
    return x >= rx and x < rx + rw and y >= ry and y < ry + rh

#Alerts program when ball hits a side wall
def hit_side_wall (x):
    return x == BALL_RADIUS or x == (WIDTH - BALL_RADIUS)

#Alerts program when ball hits top or bottom wall
def hit_wall (y):
    return y == BALL_RADIUS or y == (HEIGHT - BALL_RADIUS)

def set_paddle_color ():
    set_fill_color (1, .48, 0)
    
def set_ball_color ():
    set_fill_color (0, 0, 0)

def pong_game ():
    enable_smoothing()
    disable_stroke()
    set_clear_color (.5, .5, 1)
    clear()
    
    #coordinates for left paddle
    x_left = 0
    y_left = 0
    
    #coordinates for right paddle
    x_right = (WIDTH - BLOCK_WIDTH)
    y_right = (HEIGHT - BLOCK_HEIGHT)
    
    #starting point for ball
    ball_x = 200
    ball_y = 200
    
    #pixels ball moves
    x_speed = 3
    y_speed = 5
    
    
    while not window_closed():
        clear()
        set_paddle_color ()
        
        #draw left paddle
        draw_rectangle (x_left, y_left, BLOCK_WIDTH, BLOCK_HEIGHT)
        
        #draw right paddle
        draw_rectangle (x_right, y_right, BLOCK_WIDTH, BLOCK_HEIGHT)
    
        #Use of "if" throughout instead of "elif" allows for movement of both paddles at once
            #moves left paddle up with a
        if is_key_pressed (CONTROLS [0]) and (y_left != 0):
            y_left = y_left - BLOCK_MOVEMENT
            #moves left paddle down with z
        if is_key_pressed (CONTROLS [1]) and (y_left != HEIGHT - BLOCK_HEIGHT):
            y_left = y_left + BLOCK_MOVEMENT
            #moves right paddle up with k
        if is_key_pressed (CONTROLS [2]) and (y_right != 0):
            y_right = y_right - BLOCK_MOVEMENT
            #moves right paddle down with m
        if is_key_pressed (CONTROLS [3]) and (y_right != HEIGHT - BLOCK_HEIGHT):
            y_right = y_right + BLOCK_MOVEMENT
        
        #Changes the x and y coordinates of ball so that it moves
        ball_x += x_speed
        ball_y += y_speed
        
        #Changes y direction of ball when hits top wall
        if hit_wall (ball_y):
            y_speed *= -1
        
        #Ends the game if ball hits one of the side walls
        if hit_wall(ball_x):
            x_speed = 0
            y_speed = 0
            game_over ()

        #Draws ball
        set_ball_color ()
        draw_circle (ball_x, ball_y, BALL_RADIUS)
        
        #Changes x direction of ball when it hits right paddle
        if ball_hit_paddle ((ball_x + BALL_RADIUS), ball_y, x_right, y_right, BLOCK_WIDTH, BLOCK_HEIGHT):
            x_speed *= -1
        
        #Changes x direction of ball when it hits left paddle
        if ball_hit_paddle ((ball_x - BALL_RADIUS), ball_y, x_left, y_left, BLOCK_WIDTH, BLOCK_HEIGHT):
            x_speed *= -1
        
        request_redraw()
        sleep (.02)
    
    

start_graphics(pong_game)