from art import logo
from os import system

def auction():
    users = {}
    should_continue = True
    
    while should_continue: 
        print(logo)
        name = input("\nWhat's your name? ")
        bid = float(input("What's your bid? $ "))
        
        users[name] = bid
        
        other_user = input("Is there other user who wants to bid? 'yes' or 'no': ")
        
        if other_user.lower() == "yes":
            system('cls')
        elif other_user.lower() == "no":
            should_continue = False
            find_highest_bid(users)
    

def find_highest_bid(dictionarie):
    highest_bid = 0
    name_winner = ''
    
    for key in dictionarie:
        bid_value = dictionarie[key]
        
        if bid_value > highest_bid:
            highest_bid = bid_value
            name_winner = key
            
    print(f"\nThe user {name_winner} is the winner with ${highest_bid} of bid\n")
        
        
auction()