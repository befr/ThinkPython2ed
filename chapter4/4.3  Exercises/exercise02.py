'''
2. Add another parameter, named length, to square. 
Modify the body so length of the sides is length, 
and then modify the function call to provide a second argument. 
Run the program again. 
Test your program with a range of values for length.
'''

def square(t, length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)

import turtle

bob = turtle.Turtle()

#for testing purpose
for i in range(25, 300, 25):
    square(bob, i)

turtle.mainloop()