from Resources import MENU, resources
on = True
money = 0


def report(money):
    """Report on the current resources in the system."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def make_coffee(drink):
    """Make coffee based on user's drink choice."""
    global resources
    ingredient = MENU[drink]['ingredients']
    resources['water'] -= ingredient['water']
    resources['coffee'] -= ingredient['coffee']
    resources['milk'] -= ingredient['milk']
    print(f"Here is your {drink}☕. Enjoy!")

def check_resouces(drink):
    ingredient = MENU[drink]['ingredients']
    if resources['water'] > ingredient['water']:
        if resources['coffee'] > ingredient['coffee']:
            if resources['milk'] > ingredient['milk']:
                process_coins(drink)
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")


def process_coins(drink):
    global money
    cost = MENU[drink]['cost']
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total == cost:
        money += cost
        make_coffee(drink)
    elif total > cost:
        change = total - cost
        print(f"Here is ${round(change, 2)} dollars in change.")
        money += cost
        make_coffee(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")


while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "espresso":
        check_resouces(user_input)
    elif user_input == "latte":
        check_resouces(user_input)
    elif user_input == "cappuccino":
        check_resouces(user_input)
    elif user_input == "report":
        report(money)
    elif user_input == "off":
        on = False
