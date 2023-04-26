import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-11, 0), (-22, 0)]

for position in starting_position:
    turtle = t.Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.shapesize(0.5)
    turtle.goto(position)
    



screen.exitonclick() 