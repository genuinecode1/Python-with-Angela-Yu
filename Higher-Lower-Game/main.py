#importing
from art import logo
from art import vs
from game_data import data
import random
import os


#greetings
print("!!  Welcome to the game  !!")

#functions
def printData(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}")


def checkAnswer(guess,a,b):
    """Take the user gat and followers of account a and b and return the result"""
    temp = ""
    if(a>b):
        temp += "a"
    else:
        temp += "b"
    
    if(temp == guess):
        return True
    else:
        return False
    

score = 0
value = True
account_a = random.choice(data)
print(logo)
while(value):
    account_b = random.choice(data)

    if account_a==account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {printData(account_a)}.")
    print(vs)
    print(f"Against B: {printData(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follow_count = account_a["follower_count"]
    b_follow_count = account_b["follower_count"]
    is_correct = checkAnswer(guess,a_follow_count,b_follow_count)

    os.system('cls')
    print(logo)

    if(is_correct):
        score +=1
        print(f"You're right! Current Score: {score}.")
        account_a = account_b
        
    else:
        print(f"Sorry , that's wrong. Final Score : {score}")
        value = False