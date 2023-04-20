from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("classic")
tom.speed(7)
tom.penup()
tom.setpos(-50, 70)

colors = ['red', 'dark olive green', 'goldenrod', 'orchid', 'midnight blue', 'slate gray', 'dodger blue', 'yellow green']
comands = [tom.forward(100), tom.backward(100), tom.right(100), tom.left(100)]

'''def random_walk():
    tom.pendown()
    size = 1
    for _ in range(100):
        color = random.choice(colors)
        tom.pencolor(color)
        
        random.choice(comands)()
    tom.pensize(size)
    size += 0.3'''
    
tom.pendown()
random.choice(comands)
        






'''def draw_shapes():
    tom.pendown()
    color = ['Green', 'BlueViolet', 'Chocolate', 'DarkOrange', 'Blue', 'DarkRed', 'Lime', 'Gold']
    step = 3
    
    for i in color:
        tom.pencolor(i)
        angle = 360 / step
        
        for n in range(step):
            tom.forward(100)
            tom.right(angle)
        step += 1
        
draw_shapes() '''     

screen = Screen()
screen.exitonclick()