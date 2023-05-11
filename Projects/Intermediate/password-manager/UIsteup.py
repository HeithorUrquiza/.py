from tkinter import *

class UIsetup:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20)
        self.config_img()
        self.user_label = Label(text="User/Email:", padx=3, pady=5).grid(column=0, row=2)
        self.website_label = Label(text="Website:", padx=3, pady=5).grid(column=0, row=1)
        self.password_label = Label(text="Password:", padx=3, pady=7).grid(column=0, row=3)
        self.website_entry = Entry(width=50).grid(column=1, row=1, columnspan=2)
        self.mail_entry = Entry(width=50).grid(column=1, row=2, columnspan=2)
        self.password_entry = Entry(width=31).grid(column=1, row=3)
        self.generate_button = Button(text="Generate Password", padx=2).grid(column=2, row=3)
        self.add_button = Button(text="Add", width=42).grid(column=1, row=4, columnspan=2)


    def run_gui(self):
        self.window.mainloop()


    def config_img(self):
        self.canvas = Canvas(width=200, height=200)
        self.password_icon = PhotoImage(file="Projects/Intermediate/password-manager/change-password.png")
        self.canvas.create_image(130, 100, image=self.password_icon)
        self.canvas.grid(column=1, row=0)