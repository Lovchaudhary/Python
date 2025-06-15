Collection=set()
#print(len(Collection))
#print("after addition \n")
Collection.add(1)
Collection.add(2)
Collection.add("Apna college")
Collection.add((69,59,213,123))
#print(len(Collection))
#print(Collection)
Collection.clear()
#print("After clear \t Values will be ")
#print(len(Collection))
info= {1,2,3}
data={3,4,5,6}
#print(Collection)
#print(info.intersection(data))
# QUESTIONS
Dictionary={
  "cat" :"A small animal",
    "Table ": ["a Piece of wood ",["A multiplication set"]],
}
print(Dictionary)

Classroom={"Python","C++","Java","Java script","Python","Java","Java","C++","C"}
print(Classroom)
#MARKS OF 3 SUBHJECTS
Marks={}
x=int(input("Enter marks of phy: "))
y=int(input("Enter marks of chemistry: "))
z=int(input("Enter marks of Maths: "))
Marks.update({"Physics": x,"Chemi":y,"Maths":z,})
print(Marks)