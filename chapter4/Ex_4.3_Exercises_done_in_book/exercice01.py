'''
1. Write a function called square that takes a parameter named t, 
which is a turtle. 
It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, 
and then run the program again.
'''

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

import turtle
bob = turtle.Turtle()
square(bob)
turtle.mainloop()