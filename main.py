import zulw
import turtle

Z = zulw.Snake()

if __name__ == '__main__':

    turtle.onkey(Z.gora, 'Up')
    turtle.onkey(Z.lewo, 'Left')
    turtle.onkey(Z.prawo, 'Right')
    turtle.onkey(Z.dol, 'Down')

    turtle.listen()
    turtle.mainloop()