from art import logo
from os import system
from operations import *


def calculator():
    
    print(logo)
    num1 = float((input("Type the first number: ")))
    should_continue = False
    
    while True:
        operation = input("What's the operation: [+, -, *, /]: ")
        num2 = float((input("Type the next number: ")))
        function = operations[operation] 
        answer = function(num1, num2)
        
        print(f"\n{num1} {operation} {num2} = {answer}")
        
        action = input(f"\nType 'y' to continue calculating with {answer}, 'new' to a new calculate or 'n' to exit: ")
        
        if action == 'y':
            num1 = answer
        elif action == 'new':
            system('cls')
            calculator()
        else:
            return
            
calculator()
            
    
