'''
4. Write a function called circle that takes a turtle,
 t, and radius, r, as parameters 
 and that draws an approximate circle by calling polygon with 
 an appropriate length and number of sides. 
 
 Test your function with a range of values of r.

Hint: figure out the circumference of the circle and 
make sure that length * n = circumference.
'''

#1st discover how to calculte a circuference of a circle
#Circumference of circle = π x Diameter of circle
# Diamenter = 2 x Radius
#circumference = pi x (radius x 2)
# lenght = (pi x (radius x 2)) / n
# n = (pi x (radius x 2)) / lenght
# to perform a circle lenght / n = 1 -> n = 360

pi = 3.1415

def polygon(length, n):
    angle = 360/n
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)
        bob.fd(length)

def circle(t, r, angle):
    polygon((pi * (r * 2) / 360), 360)

import turtle

bob = turtle.Turtle()

#for testing purpose
for r in range(1, 20, 2):
    circle(bob, r)

turtle.mainloop()