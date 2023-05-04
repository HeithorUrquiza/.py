from turtle import Turtle

FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.current_level = 1
        self.show_score()
        
        
    def show_score(self):
        self.write(f"Level: {self.current_level}", False, 'left', FONT)
        
        
    def update_score(self):
        self.current_level += 1
        self.clear()
        self.show_score()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, 'center', FONT)
