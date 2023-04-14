from art import logo, vs
from game_data import data
from os import system
import random

def random_person():
    return random.choice(data)


def compare_person(followers1, followers2):
    if followers1 > followers2:
        return 'A'
    else: 
        return 'B'
    

def higher_lower_message(A, B):
    print(logo)
    print(f"\nCompare A: {A['name']}, {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
        
    

personA = random_person()
personB = random_person()
user_score = 0

should_continue = True

higher_lower_message(personA, personB)

while should_continue:
    more_follwers = compare_person(personA['follower_count'], personB['follower_count'])
    user_input = input("Which one you guess has more followers? Type 'A' or 'B': ").upper()

    if user_input == more_follwers:
        system('cls')
        user_score += 1
        personA = personB
        personB = random_person()
        
        print(f"Right choice. Current score: {user_score}")
        higher_lower_message(personA, personB)
    else:
        system('cls')
        print(f"Wrong choice. Your final score is: {user_score}")
        should_continue = False
