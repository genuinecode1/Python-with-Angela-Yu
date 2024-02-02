import  random

# Diagram
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#greetings
print("!! Welcome to Rock Paper Scissor game !!\n")

rounds = int(input("How many rounds you want in game\n"))

for i in range(rounds):
    user = int(input("Press 1 for Rock ,  Press 2 for Paper , Press 3 for Scissors\n"))
    if(user == 1):
     print("rock\n" + rock)
    elif(user == 2):
      print("paper\n"+paper)
    else:
      print("scissors" +scissors)
    computer = random.randint(1,3)
    print("\n Computer chooses :  \n")
    if(computer == 1):
     print("rock\n" + rock)
    elif(computer == 2):
      print("paper\n"+paper)
    else:
      print("scissors" +scissors)

    if(user==computer):
        print("\n--------Its a Draw-----------\n")
    else:
      if(user==1):
        if(computer==2):
          print(" !!  You Loose  !!\n")
        else:
           print("!!  You Win  !!\n")
      elif(user==2):
        if(computer==1):
          print(" !!  You Win  !!\n")
        else:
           print("!!  You Loose  !!\n")
      else:
         if(computer==1):
          print(" !!  You Loose  !!\n")
         else:
           print("!!  You Win  !!\n")

print("!!  Thank You  !!")