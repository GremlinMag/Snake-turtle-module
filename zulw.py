import turtle
import random

class Snake(turtle.Turtle):
    def init(self):
        self.shape('square')
        self.penup()
        self.turtlesize(1, 1)
    pozycja_x = 0
    pozycja_y = 0
    speed_x = 0
    speed_y = 21
    dlugosc = 3

    def gora(self):
        self.speed_x = 0
        self.speed_y = 21
    def dol(self):
        self.speed_x = 0
        self.speed_y = -21

    def lewo(self):
        self.speed_x = -21
        self.speed_y = 0

    def prawo(self):
        self.speed_x = 21
        self.speed_y = 0

    def reset(self):
        self.pozycja_x = self.pozycja_x + self.speed_x
        self.pozycja_y = self.pozycja_y + self.speed_y
        self.setpos(self.pozycja_x, self.pozycja_y)

    def bye(self):
        turtle.bye()

class Food(turtle.Turtle):
    def init(self):
        self.shape('circle')
        self.penup()
        self.color('red')
        self.turtlesize(1, 1)
        self.pozycja_x = random.randrange(-231, 240, 21)
        self.pozycja_y = random.randrange(-231, 240, 21)
        self.setpos(self.pozycja_x, self.pozycja_y)
    def zmien_lokacje(self):
        turtle.delay(0)
        self.pozycja_x = random.randrange(-231, 240, 21)
        self.pozycja_y = random.randrange(-231, 240, 21)
        self.setpos(self.pozycja_x, self.pozycja_y)

class Segment(turtle.Turtle):
    def init(self):
        self.shape('square')
        self.penup()
        self.color('grey')
        self.turtlesize(1, 1)
