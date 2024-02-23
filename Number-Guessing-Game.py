# importing libraries
import random

#greetings
print("!! Welcome to Number Guessing Game  !!")

# random number
print("\n Hey I am choosing a number between 1 and 100 & you have to guess it")
print("!!  GOOD LUCK FOR THE GAME  !!")
number  = random.randint(1,100)

# asking for level
level = input("Choose Level you want -> type easy or hard : ")
chances = 0
if(level == 'easy'):
    chances = 10
elif(level == "hard"):
    chances = 5
else:
    print("You choose a  wrong level ")

print(f"You Have {chances} to guess the number")

if level == "easy" or level == "hard":
    temp = False
    while(chances != 0):
        guess = int(input("Enter Your number : "))
        if(guess == number):
            temp = True
            break
        elif (guess > number and guess-number >5):
            chances-=1
            print("Guess is Too HIGH")
            print("Guess Again")
        elif (guess > number and guess-number <5):
            chances-=1
            print("Guess is HIGH")
            print("Guess Again")
        elif (guess < number and number-guess <5):
            chances-=1
            print("Guess is Low")
            print("Guess Again")
        elif (guess < number and number-guess >5):
            chances-=1
            print("Guess is Too Low")
            print("Guess Again")
    if(temp):
        print("\n Hurray You guessed the right number")
    else:
        print("You Failed to guess the number try again")