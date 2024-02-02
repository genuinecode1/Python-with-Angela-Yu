import random

# greetins
print("!! Welcome to Who will pay bugger  !!\n")

#taking input
names = input("Enter people names (use comma to seperate names)\n")

name = names.split(",")

length = len(name)

# printing the result
print(f"\nThe person who is going to pay the bill is {name[random.randint(0,length-1)]} \n")

print("!!  Thank You  !!")