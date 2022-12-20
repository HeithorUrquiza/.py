import random

class Gen_password():
    
    def __init__(self):
        self._lower_case = "abcdfghijklmnopqrstuvwxyz"
        self._upper_case = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
        self._numbers = "1234567890"
        self._symbols = "@#$%&*/\?"
        
    def _password(self):
        Use_for = self._lower_case + self._upper_case + self._numbers + self._symbols
        lenght_password = 10
        password = "".join(random.sample(Use_for, lenght_password))
        return password
    
    def myPassword(self):
        return self._password()
    

firstPassword = Gen_password()
print(firstPassword.myPassword())
        
        