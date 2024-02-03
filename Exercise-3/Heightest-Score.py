#greetigns
print("!  WELCOME  !!")

length = int(input("\nTotal number of students\n"))

marks = []

for i in range(length):
   marks.append(int(input()))



max_marks = 0
for i in range(length):
  if(max_marks<marks[i]):
     max_marks = marks[i]

#printing  ans
print(f"Average Height of the given numbers is {max_marks}")