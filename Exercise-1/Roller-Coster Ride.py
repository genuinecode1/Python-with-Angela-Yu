# Greetings
print("\n!!   Welcome to our Roller-Coster Ride   !!\n")

#height
height = int(input("what is you height? ( in centimeter) \n"))

#age
age = int(input("what is you age? \n"))

#photo
photo = input("Do You want Photo or not? Type Y for Yes & N for No")

#calculations
total_bill =0

if(height>120):
    if(age<12):
        total_bill += 500
    elif (age>12 and age<18):
        total_bill += 700
    elif (age>=45 and age<=55):
        total_bill += 0
    else:
        total_bill +=1200
    
    if(photo == "Y"):
        total_bill +=300

# printting answer
if(height<120):
  print("You can't allow to ride\n")
else:
  print(f"Your total bill is ₹{total_bill}\nHappy Riding")

print("!!   Thank You for choosing us   !!")
