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