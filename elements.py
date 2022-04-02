import turtle
import random

class Snake(turtle.Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.shape('square')
        self.penup()
        self.turtlesize(1, 1)

    direction = 'r'

    def go_up(self):
        if self.direction != 'd':
            self.seth(90)
            self.direction = 'u'

    def go_down(self):
        if self.direction != 'u':
            self.seth(270)
            self.direction = 'd'

    def go_left(self):
        if self.direction != 'r':
            self.seth(180)
            self.direction = 'l'

    def go_right(self):
        if self.direction != 'l':
            self.seth(0)
            self.direction = 'r'

    def reset(self):
        self.forward(21)

    def bye(self):
        turtle.bye()

class Food(turtle.Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.turtlesize(1, 1)
        self.setpos(random.randrange(-231, 252, 21), random.randrange(-231, 252, 21))
    def relokate(self):
        self.setpos(random.randrange(-231, 252, 21), random.randrange(-231, 252, 21))

class Segment(turtle.Turtle):
    def __init__(self):
        super(Segment, self).__init__()
        self.shape('square')
        self.penup()
        self.color('grey')
        self.turtlesize(1, 1)

class Border(turtle.Turtle):
    def __init__(self,  size_y, size_x, pos_y, pos_x):
        super(Border, self).__init__()
        self.speed(0)
        self.shape('square')
        self.penup()
        self.color('purple')
        self.turtlesize(size_y, size_x)
        self.setpos(pos_y, pos_x)

# end game title
class End_game(turtle.Turtle):
    def __init__(self):
        super(End_game, self).__init__()
        self.speed(0)
        self.penup()
        self.color('red')
        self.write("Game Over", move=False, align='center', font=('Arial', 60, 'normal'))
        self.color('white')

