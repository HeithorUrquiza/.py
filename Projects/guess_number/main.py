import random
from art import logo
from os import system

def randomNumber():
    return random.randint(1, 100)


def compare(number):
    guess = int(input("Make a guess: "))
    
    if guess == number:
        return 0
    elif guess - number <= 3 and guess - number >= -3:
        return "It's close"
    elif guess > number:
        return "Too high"
    elif guess < number:
        return "Too low"
    
    
def mod_game(chose, rand_number):
    if chose == 'easy':
        attempts = 10
    elif chose == 'hard':
        attempts = 5
        
    for tries in range(attempts, -1, -1):
        if tries == 0:
            print("You've run out of guesses. You lose")
            print(f"The number that I thought was: {rand_number}")
            return
        
        print(f"\nYou have {tries} attempts remaining to guess the number.")
        result = compare(rand_number)
            
        if result == 0:
            print(f"You've got it!! The number was {rand_number}") 
            return
        elif tries == 1:
            print(result)
        else:
            print(result)
            print("Guess again")
        
        
def play_game():
    is_end = False

    while not is_end:
        print(logo)
        print("\nWelcome to the Guess Number Game")
        print("I'm thinking of a number between 1 and 100. Which is it?")

        difficulty = input("Choose a difficulty: Type 'easy' or 'hard' and try guess: ").lower()
        computer_number = randomNumber()

        mod_game(chose=difficulty, rand_number=computer_number)
        
        if input("\nType 'y' to restart or 'n' to exit: ").lower() == 'n':
            is_end = True
        else:
            system('cls')
            
play_game()
            
            


