import json

class JsonDocument:
            
    def __init__(self):
        self.data_file = None
        self.data = None
            
            
    def save(self, **kw):
        new_data = {
            kw['website']: {
                "email": kw['email'],
                "password": kw['password']
            }
        }
        
        try: 
            with open("Projects/Intermediate/password-manager/data.json", "r") as self.data_file:
                self.data = json.load(self.data_file)
        except FileNotFoundError:
            with open("Projects/Intermediate/password-manager/data.json", "w") as self.data_file:
                json.dump(new_data, self.data_file, indent=4)
        else:
            self.data.update(new_data)        
            
            with open("Projects/Intermediate/password-manager/data.json", "w") as self.data_file:
                json.dump(self.data, self.data_file, indent=4)        
                
                
    def consult(self, user_entry, messagebox):
        try:
            with open("Projects/Intermediate/password-manager/data.json", "r") as self.data_file:
                self.data = json.load(self.data_file)
                self.data = self.data[user_entry]
        except FileNotFoundError:
            messagebox.showerror("Error", "No Data File Found")
        except KeyError:
            messagebox.showerror("Error", "No details for the website exists")
        else:
            messagebox.showinfo(user_entry.title(), f"Email: {self.data['email']}\nPassword: {self.data['password']}")