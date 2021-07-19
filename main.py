import zulw
import turtle
import time


if __name__ == '__main__':
    turtle.setup(483, 483)
    segments = []
    Z = zulw.Snake()
    Z.init()

    Y = zulw.Food()
    Y.init()

    move = 1
    delay=0.1
    X=0
    nuber_of_sergments_on_strart = 3


    for i in range(nuber_of_sergments_on_strart):
        Y.zmien_lokacje()
        C = zulw.Segment()
        C.init()
        segments.append(C)

    while X == 0:
        if Z.distance(Y) < 15:
            Y.zmien_lokacje()
            C = zulw.Segment()
            C.init()
            segments.append(C)


        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) != 0:
            x = Z.xcor()
            y = Z.ycor()
            segments[0].goto(x, y)


        for seg in segments[3:]:
            if Z.distance(seg) < 21:
                X=1
        if Z.xcor() < -231:
            Z.pozycja_x=231
        if Z.xcor() > 231:
            Z.pozycja_x=-252

        if Z.ycor() < -231:
            Z.pozycja_y=252
        if Z.ycor() > 231:
            Z.pozycja_y=-252


        if move == 1:
            Z.reset()

        turtle.onkey(Z.gora, 'Up')
        turtle.onkey(Z.lewo, 'Left')
        turtle.onkey(Z.prawo, 'Right')
        turtle.onkey(Z.dol, 'Down')
        turtle.onkey(Z.bye, 'q')
        turtle.onkey(Y.zmien_lokacje, 'z')


        turtle.listen()
        time.sleep(delay)

    turtle.exitonclick()