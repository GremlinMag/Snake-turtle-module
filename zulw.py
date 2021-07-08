import turtle

class Snake(turtle.Turtle):
    pozycja_x = 10
    pozycja_y = 10
    speed_x = 0
    speed_y = 10
    def gora(self):
        self.speed_x = 0
        self.speed_y = 10
    def dol(self):
        self.speed_x = 0
        self.speed_y = -10

    def lewo(self):
        self.speed_x = -10
        self.speed_y = 0

    def prawo(self):
        self.speed_x = 10
        self.speed_y = 0

    def reset(self):
        self.pozycja_x = self.pozycja_x + self.speed_x
        self.pozycja_y = self.pozycja_y + self.speed_y
        self.setpos(self.pozycja_x, self.pozycja_y)

    def bye(self):
        turtle.bye()

def lol():
    print('lol')