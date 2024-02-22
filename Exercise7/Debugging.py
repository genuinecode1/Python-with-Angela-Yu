

#given code
"""
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

  """

# here we have to compare number%2 == 0 istead of single = value beacuse we have to compare

#correct code

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


#given code 2->
"""
  year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  """

#there is a identation error in the code and we can clearly spot that before year
  
# correct code
  
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#given code 3 ->
  
"""
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
"""
#here is no particular error your code runs but when else condition runs numbers print in [] that sounds as output error but your code runs
# correct code
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])


