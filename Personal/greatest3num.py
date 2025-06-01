Num1 = int(input("Enter your numer"))
Num2 = int(input("Enter your numer"))
Num3 = int(input("Enter your numer"))
#using python fxn
Large = max(Num3,Num2,Num1)
print("Largest no is : ", Large)
#If else statement #
if(Num1>Num2):
    if(Num1>Num3):
        print("Number 1 is greatest ")
        
elif(Num2>Num1):
    if(Num2>Num3):
        print("Numer 2 is greatest ")

else:
    print("Number 3 is the greatest ")