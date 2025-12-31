import math
import matplotlib.pyplot as plt

class Turtle:
    def __init__(self, p, w):
        self.x = p[0]
        self.y = p[1]
        self.u = w[0]
        self.v = w[1]
    
    def copy(self):
        return Turtle((self.x, self.y), (self.u, self.v))

    def forward(self, distance):
        turtle = self.copy()
        turtle.x += distance * self.u
        turtle.y += distance * self.v
        plt.plot([self.x, turtle.x], [self.y, turtle.y], 'k-')
        self.x = turtle.x
        self.y = turtle.y

    def move(self, distance):
        self.x += distance * self.u
        self.y += distance * self.v

    def turn(self, angle):
        u = self.u
        v = self.v
        self.u = u * math.cos(angle) - v * math.sin(angle)
        self.v = u * math.sin(angle) + v * math.cos(angle)

    def resize(self, factor):
        u = self.u
        v = self.v
        self.u = u * factor
        self.v = v * factor

def draw_polygon(turtle, n):
    for i in range(n):
        turtle.forward(1)
        turtle.turn(2*math.pi/n)

def draw_star(turtle, n):
    for i in range(n):
        turtle.forward(1)
        turtle.turn(4*math.pi/n)

def draw_new_star(turtle, n):
    for i in range(n):
        turtle.forward(1)
        turtle.turn(math.pi - math.pi/n)

def draw_tristar(turtle, n):
    for i in range(n):
        turtle.forward(1)
        turtle.turn(2*math.pi/3)
        turtle.forward(1)
        turtle.turn(2*math.pi/n - 2*math.pi/3)

def draw_wheel(turtle, n):
    for i in range(n):
        turtle.forward(1)
        b = 2*math.pi/n
        turtle.turn(0.5*math.pi + 0.5*b)
        d = 2 * math.sin(0.5*b)
        turtle.forward(d)
        turtle.turn(0.5*math.pi + 0.5*b)
        turtle.forward(1)
        turtle.turn(math.pi)

def draw_spiral(turtle, n, a, s):
    for i in range(n):
        turtle.forward(1)
        turtle.turn(a)
        turtle.resize(s)

def shift(turtle, turtle_program, n, distance):
    for i in range(n):
        turtle_program()
        turtle.move(distance)

def spin(turtle, turtle_program, n, angle):
    for i in range(n):
        turtle_program()
        turtle.turn(angle)

def scale(turtle, turtle_program, n, factor):
    for i in range(n):
        turtle_program()
        turtle.resize(factor)

import numpy as np
class HodographTurtle:
    def __init__(self, p, v):
        self.p = np.array(p, dtype=float)
        self.v = np.array(v, dtype=float)
        self.pen = True
        self.segments = []
    
    def copy(self):
        return HodographTurtle((self.x, self.y), (self.u, self.v))

    def penup(self):
        self.pen = False
    
    def pendown(self):
        self.pen = True

    def turn(self, angle):
        v_old = self.v.copy()
        r = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        self.v = r @ v_old
        if self.pen:
            self._draw(v_old, self.v)
    
    def resize(self, factor):
        v_old = self.v.copy()
        self.v = v_old * factor
        if self.pen:
            self._draw(v_old, self.v)

    def move(self, delta):
        self.p = self.p + np.array(delta, dtype=float)

    def foward(self):
        self.p += self.v

    def _draw(self, v_old, v_new):
        a = self.p + v_old
        b = self.p + v_new
        self.segments.append((a.copy(), b.copy()))

    def draw(self):
        for a, b in self.segments:
            plt.plot([a[0], b[0]], [a[1], b[1]], 'k-')


plt.axis('equal')
plt.grid(True)
turtle = HodographTurtle((0, 0), (1, 0))
turtle.pendown()
turtle.turn(math.pi/2)
turtle.draw()
plt.show()
