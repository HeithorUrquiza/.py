from tkinter import *
from entities.quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="White", highlightthickness=0, 
                                 font=("Arial", 11, "bold"))
        self.score_label.grid(column=1, row=0, padx=3)
        
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(
            150, 
            125, 
            width=220, 
            font=("Arial", 15, "italic"), 
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_img = PhotoImage(file="Projects/Intermediate/quizzler-app/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, 
                                  command=self.is_right)
        self.true_button.grid(column=0, row=3)
        
        false_img = PhotoImage(file="Projects/Intermediate/quizzler-app/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, 
                                   command=self.is_wrong)
        self.false_button.grid(column=1, row=3)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.quiz_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
        
    def is_right(self):
        self.get_feedback(self.quiz.check_answer("True"))
        
        
    def is_wrong(self):
        self.get_feedback(self.quiz.check_answer("False"))
        
        
    def get_feedback(self, answer):
        if answer is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)        