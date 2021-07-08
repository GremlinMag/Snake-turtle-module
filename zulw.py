import turtle

class Snake(turtle.Turtle):
    def gora(self):
        self.setheading(90)
        self.forward(100)
    def dol(self):
        self.setheading(270)
        self.forward(100)

    def lewo(self):
        self.setheading(180)
        self.forward(100)

    def prawo(self):
        self.setheading(0)
        self.forward(100)

    def reset(self):
        self.setheading(90)

    def bye(self):
        turtle.bye()

def lol():
    print('lol')