#greetings
print("!  Welcome  !")

a = int(input("Enter Lower Limit\n"))
b = int(input("Enter Higher Limit\n"))

# printing ans
print("\nPrinting Even Numbers between a & b\n")
for i in range(a,b+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif (i%3 == 0):
        print("Fizz")
    elif (i%5 == 0):
        print("Buzz")
    else:
        print(i)