import random
computer =random.choice([-1,0,1])
you=int(input("Enter a number (-1, 0, 1): "))
youdict={-1:"Snake",0:"Water",1:"Gun"}
print(f"You chose {youdict[you]}")
print(f"Computer chose {youdict[computer]}")
if you==computer:
    print("It's a tie!")
elif (you==1 and computer==-1) or (you==-1 and computer==0) or (you==0 and computer==1):
    print("You win!")
elif(you==-1 and computer==1) or (you==0 and computer==-1) or (you==1 and computer==0):
    print("Computer wins!")
else:
    print("Invalid input! Please enter -1, 0, or 1.")
