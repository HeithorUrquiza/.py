from tkinter import *
from tkinter import messagebox
from utils.json_document import JsonDocument
from utils.password_generator import PasswordGenerator

class UISetup:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20)
        self.config_img()
        self.user_label = Label(text="User/Email:", padx=3, pady=5).grid(column=0, row=2)
        self.website_label = Label(text="Website:", padx=3, pady=5).grid(column=0, row=1)
        self.password_label = Label(text="Password:", padx=3, pady=7).grid(column=0, row=3)
        self.website_entry = Entry(width=34)
        self.mail_entry = Entry(width=52)
        self.password_entry = Entry(width=33)
        self.config_entries()
        self.generate_button = Button(text="Generate Password", command=self.get_password).grid(column=2, row=3)
        self.add_button = Button(text="Add", width=44, command=self.save_data).grid(column=1, row=4, columnspan=2)
        self.search_button = Button(text="Search", padx=2, width=13, command=self.find_login).grid(column=2, row=1)


    def run_gui(self):
        self.window.mainloop()


    def config_img(self):
        self.canvas = Canvas(width=200, height=200)
        self.password_icon = PhotoImage(file="Projects\Intermediate\password-manager\logo\change-password.png")
        self.canvas.create_image(130, 100, image=self.password_icon)
        self.canvas.grid(column=1, row=0)
        
        
    def config_entries(self):
        self.website_entry.grid(column=1, row=1)
        self.website_entry.focus()
        self.mail_entry.grid(column=1, row=2, columnspan=2)
        self.mail_entry.insert(END, "@gmail.com")
        self.password_entry.grid(column=1, row=3)
        
        
    def save_data(self):
        if not self.website_entry.get() or not self.password_entry.get():
            messagebox.showwarning("Error", "Please don't leave any field empty")
        else:
            data = JsonDocument()
            data.save(website=self.website_entry.get().title(), email=self.mail_entry.get(), password=self.password_entry.get())
            self.website_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.website_entry.focus()
            
            
    def find_login(self):
        data = JsonDocument()
        data.consult(self.website_entry.get().title(), messagebox)
                
                
    def get_password(self):
        new_password = PasswordGenerator()
        self.password_entry.insert(END, new_password.generate_password())