from turtle import Turtle, Screen
import random
import turtle as t



tom = Turtle()
tom.shape("classic")
tom.speed(70)
tom.penup()
t.colormode(255)
angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)


tom.pendown()
for _ in range(90):
    tom.pencolor(random_color())
    tom.circle(120)
    tom.setheading(tom.heading() + 4)
    
  

screen = Screen()
screen.exitonclick()