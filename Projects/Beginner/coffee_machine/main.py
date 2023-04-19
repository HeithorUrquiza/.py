from coffees import MENU


def check_resources(ingredients):
    """Returns True if there are sufficient ingredients or False in case there aren't"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

        
def make_payment():
    """Collect user inputs that match money"""
    print("Please, insert the coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


def process_coins(coins, drink_cost):
    """Returns change if there is or a print statement for not enough money"""
    if coins < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif coins > drink_cost:
        charge = round(coins - drink_cost, 2)
        
        print(f"Here is ${charge} in change")
        return drink_cost
    else:
        return drink_cost
    
    
def make_coffee(drink_name, ingredients):
    """Reduce ingredients from coffee machine and show a message to enjoy the coffee"""
    for item in ingredients:
        resources[item] -= ingredients[item]
        
    print(f"Here is your {drink_name}☕. Enjoy!")
    
    
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

is_on = True

while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "repport":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        
        if check_resources(drink['ingredients']):
            payment = make_payment()
            money += process_coins(payment, drink['cost'])
            
            if money > 0:
                make_coffee(choice, drink['ingredients'])         