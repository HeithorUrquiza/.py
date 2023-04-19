from art import logo, vs
from game_data import data
from os import system
import random

def random_person():
    '''Generate a random person'''
    return random.choice(data)


def compare_person(followers1, followers2):
    '''Compare followers number of two people'''
    if followers1 > followers2:
        return 'A'
    else: 
        return 'B'
    

def higher_lower_message(A, B):
    '''Format a printable message'''
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
    
    
def check_repeat(A, B):
    '''Check if the raffled people are the same'''
    while A == B:
        B = random_person()
    return B
        
        
def play_game():
    '''Run the game'''
    personB = random_person()
    should_continue = True
    user_score = 0
    
    print(logo)
    
    while should_continue:
        personA = personB
        personB = random_person()
        personB = check_repeat(personA, personB)

        higher_lower_message(personA, personB)

        more_follwers = compare_person(personA['follower_count'], personB['follower_count'])
        user_input = input("Which one you guess has more followers? Type 'A' or 'B': ").upper()

        system('cls')
        print(logo)
        
        if user_input == more_follwers:
            user_score += 1
            print(f"Right choice. Current score: {user_score}")
        else:
            print(f"\nWrong choice. Your final score is: {user_score}\n")
            should_continue = False


play_game()