from art import logo
from operations import *


def calculator():
    
    print(logo)
    num1 = float((input("Type the first number: ")))
    operation = input("What's the operation: [+, -, *, /]: ")
    num2 = float((input("Type the second number: ")))

    function = operations[operation] 
    answer = function(num1, num2)
    
    print(f"\n{num1} {operation} {num2} = {answer}")
    
    while True:
        will_continue = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
        
        if will_continue == "y":
            new_operation = input("\nPick an operation: ")
            num3 = float(input("What's the next number: "))
            function = operations[new_operation]
            new_answer = function(answer, num3)
        else: 
            return
            
        print(f"\n{answer} {new_operation} {num3} = {new_answer}")
        answer = new_answer
        
calculator()
            
    
