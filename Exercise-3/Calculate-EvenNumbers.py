#greetings
print("!  Welcome  !")

a = int(input("Enter Lower Limit\n"))
b = int(input("Enter Higher Limit\n"))

# printing ans
print("\nPrinting Even Numbers between a & b\n")
for i in range(a,b):
    if(i%2==0):
        print(str(i))
