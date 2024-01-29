
#  greetings
print("Welcome to the tip calculator ->\n")

# take information regarding total bill
bill = float(input("What was the total bill?\n"))

# take information regarding tip
tip_percentage = int(input("\nWhat percentage tip would you like to give? 10, 12, 15?\n"))

# How many people to split the bill?
persons = int(input("\nHow many people to split the bill?\n"))

# calculations
total_tip = (bill*tip_percentage)/100

total_bill = bill + total_tip

#printing ans
print(f"\nEach person should pay: {round(total_bill/persons,2)}")
