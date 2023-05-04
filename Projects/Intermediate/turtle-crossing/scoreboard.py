from turtle import Turtle

FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-190, 265)
        self.current_score = 0
        self.show_score()
        
        
    def show_score(self):
        self.write(f"Score: {self.current_score}", False, 'right', FONT)
        
        
    def update_score(self):
        self.current_score += 1
        self.clear()
        self.show_score()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, 'center', FONT)
