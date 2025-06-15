info ={
    
    "name" : "Lov chaudhary",
    "subjects" :["Python","c","C++","Java"],
    "is_adult" : "true",
    
}
students ={
    "name " :"Lov chaudhary",
    "subject" :{
        "Phy" :78,
        "chem" : 65,
        "maths" : 33,
}
}


#print(len(students))#
#print(len(list(students.keys())))#
#print(list(students.values()))
#print(students.items())
age= int(input("Enter your age "))
students.update({"age":age,"wife":"Saloni tanwar",})
print(students)