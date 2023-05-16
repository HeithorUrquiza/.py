from tkinter import *
from entities.csv_manipulator import CSVManipulator

GREEN = "#b1ddc6"

class UISetup:
    
    def __init__(self):
        self.window = Tk()
        self.data = CSVManipulator()
        self.word = None
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=GREEN)
        self.front_card = PhotoImage(file="Projects/Intermediate/flash-card/images/card_front.png")
        self.back_card = PhotoImage(file="Projects/Intermediate/flash-card/images/card_back.png")
        self.right_img = PhotoImage(file="Projects/Intermediate/flash-card/images/right.png")
        self.unknow_img = PhotoImage(file="Projects/Intermediate/flash-card/images/wrong.png")
        self.config_card()
        self.right_button = Button()
        self.unknow_button = Button()
        self.config_buttons()
        self.timer = self.window.after(3000, self.translate_card)
        self.next_card()
    
        
    def run_ui(self):
        self.window.mainloop()
        
        
    def config_card(self):
        self.canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
        self.card = self.canvas.create_image(400, 263, image=self.front_card)
        self.lenguage_text = self.canvas.create_text(400, 150, font=("Arial", 40, "italic"))
        self.word_text = self.canvas.create_text(400, 263, font=("Arial", 60, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)
        
        
    def config_buttons(self):
        self.right_button.config(image=self.right_img, highlightthickness=0, command=self.is_known)
        self.right_button.grid(column=1, row=1)
        self.unknow_button.config(image=self.unknow_img, highlightthickness=0, command=self.next_card)
        self.unknow_button.grid(column=0, row=1)
        
        
    def next_card(self):
        self.window.after_cancel(self.timer)
        self.word = self.data.get_rand_word()
        self.canvas.itemconfig(self.card, image=self.front_card)
        self.canvas.itemconfig(self.lenguage_text, fill="Black", text="English")
        self.canvas.itemconfig(self.word_text, fill="Black", text=self.word["English"])
        self.timer = self.window.after(3000, self.translate_card)
        
        
    def translate_card(self):
        self.canvas.itemconfig(self.card, image=self.back_card)
        self.canvas.itemconfig(self.lenguage_text, fill="White", text="Portuguese")
        self.canvas.itemconfig(self.word_text, fill="White", text=self.word["Portuguese"])
        
        
    def is_known(self):
        self.data.remove_word(self.word)
        self.next_card()