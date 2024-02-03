#greetigns
print("!  WELCOME  !!")

heights = input("\nEnter Height (seperated by Comma)\n")

height =heights.split(",")

length = len(height)

sum = 0
for i in range(length):
  sum += float(height[i])

sum /= length
print(f"Average Height of the given numbers is {sum}")