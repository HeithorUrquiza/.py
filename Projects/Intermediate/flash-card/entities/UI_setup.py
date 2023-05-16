from tkinter import *
from entities.csv_manipulator import CSVManipulator

GREEN = "#b1ddc6"

class UISetup:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=GREEN)
        self.config_card()
        self.right_button = Button()
        self.unknow_button = Button()
        self.config_buttons()
        
        
    def run_ui(self):
        self.window.mainloop()
        
        
    def config_card(self):
        self.canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
        self.card_front = PhotoImage(file="Projects/Intermediate/flash-card/images/card_front.png")
        self.canvas.create_image(400, 263, image=self.card_front)
        self.lenguage_text = self.canvas.create_text(400, 150, text="English", fill="Black", font=("Arial", 40, "italic"))
        self.word_text = self.canvas.create_text(400, 263, text="Example", fill="Black", font=("Arial", 60, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)
        
        
    def config_buttons(self):
        self.right_img = PhotoImage(file="Projects/Intermediate/flash-card/images/right.png")
        self.unknow_img = PhotoImage(file="Projects/Intermediate/flash-card/images/wrong.png")
        self.right_button.config(image=self.right_img, highlightthickness=0, command=self.csv)
        self.right_button.grid(column=1, row=1)
        self.unknow_button.config(image=self.unknow_img, highlightthickness=0)
        self.unknow_button.grid(column=0, row=1)
        
        
    def csv(self):
        data = CSVManipulator()