from art import logo
from os import system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_alphabet = len(alphabet) - 1

def ceaser(text_input, shift_input, direction_input):
    message = []
    position = 0
    
    if shift_input > 26:
        shift_input = shift_input % 26
    
    if direction_input == 'decode':
        shift_input *= -1
    
    for letter in text_input:
        if letter not in alphabet:
            message.append(letter)
        else:
            position = alphabet.index(letter.lower()) + shift_input
        
            if position > len_alphabet:
                message.append(alphabet[(position - len_alphabet) - 1])
            else:
                message.append(alphabet[position])
               
    print(f"Your {direction_input}d message is: {''.join(message)}")
    
    
def start():
    should_continue = True
    
    while should_continue:
        print(logo) 
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        ceaser(text_input=text, shift_input=shift, direction_input=direction) 
        
        answer = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
        
        if answer.lower() == 'no':
            should_continue = False
            print("\nSee ya!!")
            
        elif answer.lower() == 'yes':
            system('cls')
            continue
        
start()