from turtle import Turtle, Screen

# ----------- Etch A Sketch ---------------------
# w = forward  s = backwards  a = counter-clockwise  d = clockwise c = clear drawing

def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(30)


def clockwise():
    tim.right(30)


def clear_screen():
    tim.reset()
    # tim.clear()
    # tim.penup()
    # tim.setx(0)
    # tim.sety(0)
    # tim.pendown()
    # tim.setheading(0)


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
