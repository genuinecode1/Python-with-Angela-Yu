import os
 
# Clearing the Screen
os.system('cls')

from art import logo
print(logo)

bids = {}
def find_highest_bidder(bids_record):
    highest_bid = 0
    winner = ""

    for bidder in bids_record:
        bid_amount = bids_record[bidder]
        if(bid_amount>highest_bid):
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

temp =True
while(temp):
    name = input("What is your name?:  ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    any_else = input("Are there any other bidders? Tye 'yes' or 'no'.")
    if(any_else=="no"):
        temp = False
    elif any_else=="yes":
        os.system('cls')

find_highest_bidder(bids)

