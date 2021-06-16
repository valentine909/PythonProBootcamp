from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(50)


def move_backward():
    t.backward(50)


def rotate_cw():
    t.right(10)


def rotate_ccw():
    t.left(10)


def clear():
    t.home()
    t.clear()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=rotate_ccw)
screen.onkey(key='d', fun=rotate_cw)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
