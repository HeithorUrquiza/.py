from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, coordeniates):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=3.5, stretch_len=0.5)
        self.goto(x=coordeniates[0], y=coordeniates[1])
        
    
    def go_up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)
    
    
    def go_down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)
