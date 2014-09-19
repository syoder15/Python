#Sam Yoder
#10/18/12
#At least need x, y, v_x, v_y, and mass

from cs1lib import *

class Body:
    def __init__ (self, mass, start_x, start_y, x_velocity, y_velocity, pixel_radius, r, g, b):
        self.x = start_x
        self.y = start_y
        self.pixel_radius = pixel_radius
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.r = r
        self.g = g
        self.b = b
        self.mass = mass
    
    #Updates position of the body by adding the x and y velocities to the x and y coordinates
    #takes timestep into account since using really slow planets, can speed them up
    def update_position (self, timestep):
        self.x += self.x_velocity * timestep
        self.y += self.y_velocity * timestep
    
    #Updates velocity of x and y directions by adding the acceleration to each of them
    #Again, uses timestep to make it go by quicker
    def update_velocity (self, accel_x, accel_y, timestep):
        self.x_velocity += accel_x * timestep
        self.y_velocity += accel_y * timestep
    
    
    #Draws the bodies, but makes it so that 0, 0 is in the center of the screen, and takes the 
    #pixels per meter because planets are hugely separated
    def draw (self, cx, cy, pixels_per_meter):
        set_fill_color (self.r, self.g, self.b)
        draw_circle (self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)
    
    
    
    