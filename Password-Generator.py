import random

# greetings
print("!!  Welcome to Password Generator  !!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = int(input("Enter total letter you want\n"))
symbol = int(input("\nEnter total characters you want\n"))
number = int(input("\nEnter total numbers you want\n"))
level = input("\nEnter level you want (Eazy or Hard)\n")

if level =="Eazy":
    # Eazy Level
    password = ""

    for char in range(1, letter + 1):
      password += random.choice(letters)

    for char in range(1, symbol + 1):
      password += random.choice(symbols)

    for char in range(1, number + 1):
      password += random.choice(numbers)

    print(password)

elif level == "Hard":
    # Hard Level
    password_list=[]

    for char in range(1, letter + 1):
     password_list.append(random.choice(letters))

    for char in range(1, symbol + 1):
     password_list += random.choice(symbols)

    for char in range(1, number + 1):
     password_list += random.choice(numbers)


    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"\nYour password is: {password}")

