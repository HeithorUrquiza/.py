from turtle import Turtle

ALIGN = 'Center'
FONT = ('Courier', 40, 'bold')
MSG = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(100, 230)
        self.write(self.r_score, False, ALIGN, FONT)
        self.goto(-100, 230)
        self.write(self.l_score, False, ALIGN, FONT)
        self.goto(0, -290)
        self.setheading(90)
        
        for n in range(59):
            self.pensize(4.5)
            if n % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(10)
        self.penup()
        
        
    def increase_r_score(self):
        self.r_score += 1
        self.update_score()
        
        
    def increase_l_score(self):
        self.l_score += 1
        self.update_score()
        
        
    def game_over(self):
        if self.r_score > self.l_score:
            self.goto(140, 95)
            self.write(f"Right side \nWIN!!", False, ALIGN, MSG)
        if self.r_score < self.l_score:
            self.goto(-140, 95)
            self.write(f"Left side \nWIN!!", False, ALIGN, MSG)
        if self.r_score == self.l_score:
            self.goto(140, 95)
            self.write(f"DRAW", False, ALIGN, MSG)
            self.goto(-140, 95)
            self.write(f"DRAW", False, ALIGN, MSG)