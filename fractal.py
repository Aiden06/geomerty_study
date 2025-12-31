from turtle_program import Turtle, draw_polygon, draw_star, draw_new_star, draw_tristar, draw_wheel, draw_spiral, shift, spin, scale
import matplotlib.pyplot as plt
import math

def poly(turtle, n, length, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.turn(angle)

def sierpinski(turtle, n, level):
    if level == 0:
        poly(turtle, n, 1, 2*math.pi/n)
    else:
        for i in range(n):
            turtle.resize(0.5)
            sierpinski(turtle, n, level-1)
            turtle.resize(2)
            turtle.move(1)
            turtle.turn(2*math.pi/n)

def sierpinski_1(turtle, n, level, ratio = 0.4):
    if level == 0:
        poly(turtle, n, 1, 2*math.pi/n) 
    else:
        for i in range(n):
            turtle.resize(ratio)
            sierpinski_1(turtle, n, level-1, ratio)
            turtle.resize(1/ratio)
            turtle.forward(1)
            turtle.turn(2*math.pi/n)

def basic_2(turtle):
    poly(turtle, 4, 1, 0.5*math.pi)
    len = 1/3
    turtle.move(len)
    turtle.turn(0.5*math.pi)
    turtle.move(len)
    turtle.turn(-0.5*math.pi)
    poly(turtle, 4, len, 0.5*math.pi)
    turtle.move(-len)
    turtle.turn(-0.5*math.pi)
    turtle.move(len)
    turtle.turn(0.5*math.pi)

def sierpinski_2(turtle, level, row = 3):
    if level == 0:
        basic_2(turtle)
    else:
        for i in range(row*row - 1):
            turtle.resize(1/row)
            sierpinski_2(turtle, level-1, row)
            turtle.resize(row)
            turtle.move(1/row)
            if i > 0 and i % (row-1) == 0:
                turtle.turn(0.5*math.pi)
                turtle.move(1/row)        
        turtle.move(1/row)
        turtle.turn(0.5*math.pi)

def hilbert_basic(turtle, level):
    if level == 0:
        return
    else:
        turtle.turn(0.5*math.pi)
        hilbert_basic_reverse(turtle, level-1)
        turtle.forward(1)
        turtle.turn(-0.5*math.pi)
        hilbert_basic(turtle, level-1)
        turtle.forward(1)
        hilbert_basic(turtle, level-1)
        turtle.turn(-0.5*math.pi)
        turtle.forward(1)
        hilbert_basic_reverse(turtle, level-1)
        turtle.turn(0.5*math.pi)

def hilbert_basic_reverse(turtle, level):
    if level == 0:
        return
    else:
        turtle.turn(-0.5*math.pi)
        hilbert_basic(turtle, level-1)
        turtle.forward(1)
        turtle.turn(0.5*math.pi)
        hilbert_basic_reverse(turtle, level-1)
        turtle.forward(1)
        hilbert_basic_reverse(turtle, level-1)
        turtle.turn(0.5*math.pi)
        turtle.forward(1)
        hilbert_basic(turtle, level-1)
        turtle.turn(-0.5*math.pi)

plt.axis('equal')
plt.grid(True)
turtle = Turtle((0, 0), (1, 0))
hilbert_basic(turtle, 6)
plt.show()