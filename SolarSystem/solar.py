#Sam Yoder
#10/21/12
#Solar System Lab
#Credit to Devin Balkcom for his earthmoon.py

from cs1lib import *
from time import sleep
from system_class import System
from body_class import Body

EM = 5.9736e24
AU = 1.49598e11
SUNMASS = 1.98892e30

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

TIME_SCALE = 1000000.         # how many real seconds for each second of simulation
PIXELS_PER_METER = 1. / 1e9  # distance scale for the simulation

FRAME_RATE = 30.0             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

def main():
    sun = Body (1.98892e30, 0, 0, 0, 0, 35, 1, .8, 0)
    mercury = Body (EM * .06, AU * 0.3871, 0, 0, 47890, 4, .47, .4, .3)
    venus = Body (EM * .82, AU * 0.7233, 0, 0, 35040, 11, .95, .28, 0)
    earth = Body (EM, AU, 0, 0, 29790, 12, 0, 0, 1)
    mars = Body (EM * 0.11, AU * 1.524, 0, 0, 24140, 6, 1, .03, 0)
    solarsystem = System([sun, mercury, venus, earth, mars])
    
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    while not window_closed(): 
        clear()
        
        # Draw the system in its current state.
        solarsystem.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    
        # Update the system for its next state.
        solarsystem.update(TIMESTEP * TIME_SCALE)
   
        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Solar System simulation", WINDOW_WIDTH, WINDOW_HEIGHT)
