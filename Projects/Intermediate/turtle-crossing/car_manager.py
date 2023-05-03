from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.setheading(180)
        self.starting_position()
        

    def starting_position(self):
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
        
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)