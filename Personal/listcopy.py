list=[1,2,1]
#list.append(input("Enter a list "))#

copiedlist=list.copy()
copiedlist.reverse()
    
if(list==copiedlist):
    print("This is a Pellendrome ")
else:
    print("This is not a pellendromne ")
    