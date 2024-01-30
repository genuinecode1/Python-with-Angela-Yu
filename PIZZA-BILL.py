#  greetings
print("!!   Welcome to the our store   !!\n")

# take information regarding size
size = input("Wwhat size you want ?\n")

# take information regarding pepperoni
pep = input("\nDo you want pepperoni in your Pizza ? Press Y for yes and N for No.\n")

# Cheese or not
cheese = input("\nDo you want cheese in your Pizza ? Press Y for yes and N for No.\n")

# calculations
total_bill = 0

if(size=="small"):
 total_bill += 1500
elif ( size=="medium"):
 total_bill += 2000
else:
 total_bill += 2500

if(pep=="Y"):
  if(size=="small"):
   total_bill+=200
  else:
   total_bill+=300

if(cheese == "Y"):
 total_bill += 100


#printing ans
print(f"\n\n total bill of your pizza is ₹{total_bill}\n")
print("!!   Thank you for choosing us   !!")
