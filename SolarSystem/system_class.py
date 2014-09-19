#Sam Yoder
#10/18/12

from math import sqrt

GRAV = 6.67384e-11
#distance = sqrt(((i+1.x - i.x)(i+1.x - i.x)) + (i+1.y - i.y)(i+1.y - i.y))

class System:
    def __init__ (self, body_list):
        self.body_list = body_list
    
    #Computes the acceleration by determining the distance between each planet
    #and then it figures out the x acceleration and y acceleration and returns
    #a tuple
    def __compute_acceleration (self, i):
        accel_x = 0
        accel_y = 0
        for body in self.body_list:
            if body != i :
                #top of acceleration equation
                top = GRAV * body.mass
                #x distance and y distance
                x_dist = body.x - i.x
                y_dist = body.y - i.y
                #total distance (distance between two points equation
                distance = sqrt(x_dist * x_dist + y_dist * y_dist)
                #acceleration
                a = top / (distance*distance)
                #x and y accelerations
                accel_x += a * x_dist / distance
                accel_y += a * y_dist / distance
        return (accel_x, accel_y)
    
    #Updates each of the bodies in the system by computing the accelerations and
    #then updating the velocity and the positions of the bodies
    def update (self, timestep):
        for body in self.body_list :
            (accel_x, accel_y) = self.__compute_acceleration (body)
            body.update_velocity (accel_x, accel_y, timestep)
            body.update_position (timestep)
            

    #Draws every body in the system, has same parameters as draw in Body class
    #so that they can work
    def draw (self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)