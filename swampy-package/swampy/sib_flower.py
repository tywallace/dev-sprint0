# Flower excercise (4.2) from Week 0

# Name:

from math import pi
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()

def polyline(turtle,n,length,angle):
	for i in range(n):
		fd(turtle, length)
		lt(turtle, angle)

def arc(turtle,radius,angle):
	arc_length = 2*pi*radius*angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(turtle, n, step_length, step_angle)


def petal(turtle,length, curve):
	for i in range(2):
		arc(turtle,length,curve)
		lt(turtle,180-curve)


def flower(turtle, length, angle, number):
	for i in range(number):
		petal(turtle,length, angle)
		lt(turtle,360.0/number)

def move(turtle,length):
	pu(turtle)
	fd(turtle,length)
	pd(turtle)


bob.delay = 0.01

move(bob,-100)
flower(bob,60,60,7)
move(bob,100)
flower(bob,40,80,10)
move(bob,100)
flower(bob,140,20,20)



wait_for_user()					

