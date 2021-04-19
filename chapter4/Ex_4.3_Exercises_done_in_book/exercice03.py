'''
3. Make a copy of square and change the name to polygon. 
Add another parameter named n and 
modify the body so it draws an n-sided regular polygon. 

Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
'''

def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)
        bob.fd(length)

import turtle

bob = turtle.Turtle()

n_sides = 7 #number of side 

#for testing purpose
for i in range(30, 50, 5):
    polygon(bob, i, n_sides)

turtle.mainloop()