import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def hit(list_card):
    while True:
        answer = input("Do you wanna get another card? ").lower()
            
        if answer == "yes":
            list_card.append(deal_card())
        else:
            return list_card
     
        
def calculate_score(user, computer):
    users_score = sum(user)
    computers_score = sum(computer)
    
    if users_score == 21:
        return 0
    elif users_score > 21:
        return 1
    elif users_score > 21 and user.__contains__(11):
        user[user.index(11)] = 1
        users_score = sum(user)
        
        if users_score > 21:
            return 1
        elif users_score < 21:
            user = hit()
            users_score = sum(user)
    elif users_score < 21:
            user = hit()
            users_score = sum(user)
            
    if computers_score == 21:
        return 1
    elif computers_score > 21:
        return 0
    elif computers_score > 21 and computers_score.__contains__(11):
        computer[computer.index(11)] = 1
        computers_score = sum(computer)
        
        if computers_score > 21:
            return 0
        elif computers_score < 21:
            computer = hit()
            computers_score = sum(computer)    
    elif computers_score < 17:
        computer = hit()
        computers_score = sum(computer)
        
    if users_score > computers_score:
        return 0
    elif users_score < computers_score:
        return 1
    else:
        return 2    


def play():
    print(logo)
    users_cards = []
    computers_cards = []

    users_cards.append(deal_card())
    users_cards.append(deal_card())
    computers_cards.append(deal_card())
    computers_cards.append(deal_card())
    
    print("")


    
    
    