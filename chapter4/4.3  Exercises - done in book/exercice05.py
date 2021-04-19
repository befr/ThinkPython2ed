'''
5. Make a more general version of circle called arc that 
takes an additional parameter angle, 
which determines what fraction of a circle to draw.

 angle is in units of degrees, 
 so when angle=360, arc should draw a complete circle
'''

# from the book - this is not mine =/

import turtle
import math

#1st verison - works by itself
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#re-organized (and best versions, generalized, from previous execicies)
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)    

#for testing it
bob = turtle.Turtle()
arc(bob, 50, 150)    
circle(bob, 55)

turtle.mainloop()