#greetings
print("!!  Welcome to Area Caculator  !!\n")



#function to calculate area
def Area(length,breadth):
    Area = length*breadth
    print(f"\nArea of the given shape is {Area}")

def Area2(Radius,Height):
    Area = Radius*Radius*Height*(22/7)
    print(f"\nArea of the given shape is {Area} SqUnit")



#take data from user
shape = input("Enter Shape : Reactangle, Square, Circle, Cylinder\nC")

if(shape=="Rectangle"):
    length = float(input("Enter Length:   "))
    breadth = float(input("Enter Breadth:   "))
    Area(length,breadth)
elif(shape=="Square"):
    length = float(input("Enter Side:   "))
    Area(length,length)
elif(shape=="Circle"):
    length = float(input("Enter Radius:   "))
    Area2(length,1)
else:
    length = float(input("Enter Radius:   "))
    Height = float(input("Enter Radius:   "))
    Area2(length,Height)