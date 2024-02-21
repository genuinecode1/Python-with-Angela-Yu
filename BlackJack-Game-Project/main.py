#importing libraries
from art import logo
import random
import os

#Function for draw a random card from the deck
def deal_card():
    """ Returns a  random card from the deck of the cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#calculate sum of the list
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and sum(cards)>21:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards) 

#comparing the score & declare the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "The game is DRAW"
    elif computer_score == 0:
        return "You Lose, opponent has Blackjack "
    elif user_score==0:
        return "Hurray You Win with a Blackjack"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over. You Win"
    elif user_score>computer_score:
        return "Hurray You Win"
    else:
        return "You lose"
    
def play_game():
    # Declaration of the user and computer cards list
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #calculate scores
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")


        if user_score==0 or comp_score ==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal =="y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score<17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score : {user_score}")
    print(f"   computer's final hand: {computer_cards}, final score: {comp_score}")
    print(compare(user_score,comp_score))


#restart or not
while input("Do you want to play game of Blackjack? Type 'y' or 'n': ")=='y':
    os.system('cls')
    play_game()

