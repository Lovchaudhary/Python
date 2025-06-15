#x=int(input("Enter the range"))
#y=int(input("Enter the Ending range"))
#step=int(input("How much increment"))
#seq = range(x,y)
 #for i in seq:
     #print(" ",step,"*",i,"= " ,i * step)




n=int(input())
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Total sum is ",sum)
fact =1
i=1
while i<=n:
    fact*=i
    i+=1
print("Total fact is ",fact)
i=1
for i in range(1,n+1):
    fact*=1
    
print("fact = : ",fact)

