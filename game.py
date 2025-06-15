import random
target = random.randint(1,100)
while True:
    userinput=input("Guess a number or To quit press (Q) ")
    if(userinput=="Q"):
        break
    userinput=int(userinput)
    if(userinput== target):
        print("-------SUCCESSFUL------- "
              "Correct Guesss.......")
        break
    elif(userinput<target):
        print("the numer is too small take a new number")
    else:
        print("The number is too big  ")
    
print("---------GAME OVER-------")