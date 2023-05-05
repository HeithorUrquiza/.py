from turtle import Turtle

ALIGNING = 'center'
FONT = ('Arial', 7, 'italic')

class Writer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('Black')
        
        
    def write_name(self, x, y, state):
        self.goto(x, y)
        self.write(state, align=ALIGNING, font=FONT)