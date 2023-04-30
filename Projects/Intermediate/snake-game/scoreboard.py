from turtle import Turtle

ALIGN = "center"
FONT = ("Lexend", 14, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0.0, 268)
        self.speed("fastest")
        self.color("white")
        self.write_score()
        
        
    def increase(self):
        self.score += 1
        self.clear()
        self.write_score()
        
    
    def write_score(self):
        self.write(f"Score:  {self.score}", False, ALIGN, FONT)
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, ALIGN, FONT)