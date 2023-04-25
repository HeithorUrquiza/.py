import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    """ Move the turtle forward """
    tim.forward(11)
    
    
def move_backward():
    """ Move the turtle backward """
    tim.backward(11)
    
    
def turn_right():
    """ Turn the turtle to right """
    tim.setheading(tim.heading() - 10)
    
    
def turn_left():
    """ Turn the turtle to left """
    tim.setheading(tim.heading() + 10)


def clear_screen():
    """ Clean the screen and reset the position of the turtle """
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()