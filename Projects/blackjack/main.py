import random
from os import system
from art import logo

def deal_card():
    '''Return a random card from the deck '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
        
def calculate_score(cards):
    '''Take a list of cards and calculated the sum of their values. If the score is 21 return 0, else return the sum'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def compare(score_user, score_computer):
    if score_user == score_computer:
        return "\n  It's a draw 😜"
    elif score_computer == 0:
        return "\n  The computer has a Balckjack! You lose 😢"
    elif score_computer > 21:
        return "\n  The computer went out! You win 😁"
    elif score_user == 0:
        return "\n  You have a Balckjack! You win 😁"
    elif score_user > 21:
        return "\n  Wow you went out! You lose 😢"
    elif score_user > score_computer:
        return "\n  You win with highest score 😁"
    else:
        return "\n Sorry you lose 😢. The computer has more score"


def play():
    print(logo)
    users_cards = []
    computers_cards = []
    is_game_over = False

    for _ in range(2):
        users_cards.append(deal_card())
        computers_cards.append(deal_card())

    while not is_game_over:
        users_score = calculate_score(users_cards)
        computers_score = calculate_score(computers_cards)

        print(f"  Your cards: {users_cards}, current score: {users_score}")
        print(f"  Computer's first card: {computers_cards[0]}")

        if users_score == 0 or computers_score == 0 or users_score > 21:
            is_game_over = True
        else:
            if input("\nType 'y' to draw another card or 'n' to pass: ").lower() == 'y':
                users_cards.append(deal_card())
                users_score = calculate_score(users_cards)
                print(" ")
            else:
                is_game_over = True

    while computers_score != 0 and computers_score < 17:
        computers_cards.append(deal_card())
        computers_score = calculate_score(computers_cards)
        
    print(f"\n Your final hand: {users_cards}, final score: {users_score}")
    print(f" Computer's final hand: {computers_cards}, final score: {computers_score}")
    print(compare(score_user=users_score, score_computer=computers_score))


if input("\nDo you wanna play a BalckJack? [y / n]: ").lower() == 'y':
    do_again = True
    
    while do_again:
        system('cls')
        play()
        
        if input("\nType 'y' to restart or 'n' to exit: ").lower() == 'n':
            do_again = False
else:
    pass