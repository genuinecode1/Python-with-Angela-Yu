#greetings
print("!!  Welcome to Area Caculator  !!\n")


#function of prime number checker
def isPrime(number):
    temp = True
    for i in range(2,number-1):
       if(number % i==0):
           temp = False
           break
       else:
           continue
    if(temp==True):
      print(f"\n{number} is a prime number\n")
    else:
       print(f"\n{number} is a non prime number\n")


#taking input from user

number = int(input("Enter Number:   "))
isPrime(number)