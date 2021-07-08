import zulw
import turtle
import time


if __name__ == '__main__':
    turtle.screensize(500, 500)
    segments = []
    Z = zulw.Snake()
    Z.init()

    Y = zulw.Food()
    Y.init()


    delay=0.1
    while True:
        turtle.onkey(Z.gora, 'Up')
        turtle.onkey(Z.lewo, 'Left')
        turtle.onkey(Z.prawo, 'Right')
        turtle.onkey(Z.dol, 'Down')
        turtle.onkey(Z.bye, 'q')
        turtle.onkey(Y.zmien_lokacje, 'z')

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) != 0:
            x = Z.xcor()
            y = Z.ycor()
            segments[0].goto(x, y)
        Z.reset()
        if Z.distance(Y) < 15:
            Y.zmien_lokacje()
            C = zulw.Segment()
            C.init()
            segments.append(C)

        turtle.listen()
        time.sleep(delay)
