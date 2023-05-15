from random import choice, shuffle, randint
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class PasswordGenerator:
    
    def __init__(self):
        self.password_list = []
        
        
    def generate_password(self):
        password = ""
        new_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
        new_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
        new_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
        
        self.password_list = new_letters + new_symbols + new_numbers
        
        shuffle(self.password_list)
        password = "".join(self.password_list)
        pyperclip.copy(password)
        
        return password