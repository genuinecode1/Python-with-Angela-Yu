# Greetings
print("Welcome, Here you can able to calculate your BMI")

#height
height = float(input("what is you height? ( in meter) \n"))

#weight
weight = int(input("what is you weight? ( in kilograms) \n"))

#Calculation
BMI = weight / (height ** 2)

#ans printing
print("Your BMI score is :" + str(BMI))

if BMI<20:
    print("\nYou are underweight")
elif BMI<25:
    print("\nYou are normal weight")
elif BMI<30:
    print("\nYou are underweight")
else:
    print("\nYou are obese")