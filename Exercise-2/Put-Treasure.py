import random

#greetings
print("!!  Welcom to the Treasure Putter  !!")


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

row = int(position[0])
col = int(position[1])
if(row<=3 and col<=3):
 map[col-1][row-1] = "X"
else:
 print("\n  You choose wrong row or column  \n")



print(f"{row1}\n{row2}\n{row3}")