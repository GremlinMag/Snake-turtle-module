import elements
import turtle
import time


if __name__ == '__main__':
    # def turtle settings
    turtle.title('Snake')
    turtle.setup(540, 540, startx=200, starty=200)
    turtle.delay(0)

    # Setup borders
    elements.Border(2, 28, 0, -262)
    elements.Border(2, 28, 0, 262)
    elements.Border(28, 2, -262, 0)
    elements.Border(28, 2, 262, 0)

    # def elementary elements and params
    snake = elements.Snake()
    food = elements.Food()
    segments = []
    delay=0.1
    start_game = 1
    nuber_of_segments_on_start = 3

    # create a certain number of segments
    for _ in range(nuber_of_segments_on_start):
        el = elements.Segment()
        segments.append(el)

    # main loop
    while start_game == 1:
        # check collision with food
        if snake.distance(food) < 1:
            food.relokate()
            C = elements.Segment()
            segments.append(C)

        # change position  of segments
        for seg in range(len(segments)-1, 0, -1):
            x = segments[seg - 1].xcor()
            y = segments[seg - 1].ycor()
            segments[seg].goto(x, y)
        if len(segments) != 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y)

        # update position of snake
        snake.reset()

        # check collision with segments of snake
        for seg in segments[1:]:
            if snake.distance(seg) < 20:
                start_game = 0

        # check collision with borders
        if snake.xcor() <= -252:
            snake.setx(231)
        if snake.xcor() >= 252:
            snake.setx(-231)
        if snake.ycor() <= -252:
            snake.sety(231)
        if snake.ycor() >= 252:
            snake.sety(-231)

        # def of snake movement
        turtle.onkey(snake.go_up, 'Up')
        turtle.onkey(snake.go_left, 'Left')
        turtle.onkey(snake.go_right, 'Right')
        turtle.onkey(snake.go_down, 'Down')

        # extra keys
        turtle.onkey(snake.bye, 'q')
        turtle.onkey(food.relokate, 'z')

        # listen keys event
        turtle.listen()
        time.sleep(delay)

    # end game title
    elements.End_game()
    turtle.exitonclick()