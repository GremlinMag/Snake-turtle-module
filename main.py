import zulw
import turtle



if __name__ == '__main__':
    turtle.screensize(500, 500)
    Z = zulw.Snake()
    Z.init()

    Y = zulw.Food()
    Y.init()
    while True:
        turtle.delay(80)
        turtle.onkey(Z.gora, 'Up')
        turtle.onkey(Z.lewo, 'Left')
        turtle.onkey(Z.prawo, 'Right')
        turtle.onkey(Z.dol, 'Down')
        turtle.onkey(Z.bye, 'q')
        turtle.onkey(Y.zmien_lokacje, 'z')
        Z.reset()


        turtle.listen()
