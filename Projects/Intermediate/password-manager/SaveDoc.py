class SaveDoc:
    
    def __init__(self):
        self.file = open("Projects/Intermediate/password-manager/data.txt", "a")
        
        
    def save(self, **kw):
        self.file.write(f"{' ' * 4}{kw['website']}{' ' * 5}|{' ' * 4}{kw['email']}{' ' * 5}|{' ' * 4}{kw['password']}\n")
        self.file.close()