# Polygon excercise from Week 0

# Name:


from TurtleWorld import *
from math import pi
world = TurtleWorld()			
bob = Turtle()				


def square(turtle,length):
    for i in range(4):
        fd(turtle,length)
        lt(turtle)

def polygon(turtle,length,sides):
    for i in range(sides):
        fd(turtle,length)
        lt(turtle,360/sides)

def circle(turtle, radius):
    for i in range(360):
        fd(turtle, (2*radius*pi)/360)
        lt(turtle,1)

def arc(turtle, radius, theta):
    for i in range(theta):
        fd(turtle, (2*radius*pi)/360)
        lt(turtle,1)
        

def shape(turtle,turns,circum):
    for i in range(turns):
        fd(turtle,circum/turns)
        lt(turtle,360/turns)


bob.delay = 0.01
shape(bob,5,200)










wait_for_user()					
