import zulw
import turtle



if __name__ == '__main__':
    Z = zulw.Snake()
    Z.shape('square')
    Z.penup()
    Y = zulw.Snake()


    while True:
        turtle.onkey(Z.gora, 'Up')
        turtle.onkey(Z.lewo, 'Left')
        turtle.onkey(Z.prawo, 'Right')
        turtle.onkey(Z.dol, 'Down')
        #Z.reset()
        turtle.delay(100)

        turtle.listen()
