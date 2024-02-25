
# greetings
print("!! Hey their is your coffee machine  !!")

MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Check there is enough resources for coins"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.25
    total += int(input("How many pennies?: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns payment is accepted or declined"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct thr required ingredient from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True


def fill_resource():
    water = int(input("Water Amount(ml): "))
    milk = int(input("Milk Amount(ml): "))
    coffee = int(input("Coffee Amount(gm): "))
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee


while is_on:
    choice = input("What Would You like? (expresso/cappuccino/latte): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        add = input("Are you want to add resources (type yes or no): ")
        if add == "yes":
            fill_resource()
    elif choice != "expresso" or choice != "cappuccino" or choice != "latte":
        print("Invalid input")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
