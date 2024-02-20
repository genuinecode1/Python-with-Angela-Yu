
from Art import logo
print(logo)

#greetongs 
print("\n!!  Welccome to our calcultor service  !!")

#Add
def add(num1,num2):
    return num1+num2

#Sub
def sub(num1,num2):
    return num1-num2

#Mul
def mul(num1,num2):
    return num1*num2

#Div
def div(num1,num2):
    return num1/num2

#power
def power(num1,num2):
    return num1**num2

#dictionary for all operation
operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "^":power,
}
def calculator():
   
    num1 = int(input("What is the first number: "))
    for key in operations:
            print(key)

    calculation(num1)

def calculation(num1):
    new = False  
    flag = True   
    while(flag):
        op = input("Type your operation: ")
        function = operations[op]
        num2 = int(input("What is the another number: "))


        ans = function(num1,num2)

        print(f"\n The result of {num1} & {num2} with {op} is {ans}\\n")
        next = input(f"If you do another operation with {ans} type y or exit to type e or start a new calculation type s ")
        if(next == 'y'):
            num1 = ans
        elif (next == "e"):
            flag = False
        elif(next == 's'):
            new = True
            flag = False
    
    if(new):
        calculator()

calculator()


