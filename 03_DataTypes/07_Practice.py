#Store following word meanings in a python dictionary --> table: "a piece of furniture", "list of facts & figures" \n cat: "a small animal"
meanings = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(type(meanings["table"]))

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students. --> "python","java","C++","python","javascript","java","python","java","C++","C"
subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks ={}
phy = int(input("Enter your physics marks: "))
chem = int(input("Enter your chemistry marks: "))
math = int(input("Enter your math marks: "))
marks.update({"phy" : phy})
marks.update({"chem":chem})
marks.update({"math":math})
print(marks)

#print {9 , 9.0} in a set
values = {9, "9.0"}#method 1
values = {     #with data type
    ("float", 9.0),
    ("int", 9)
}
print(values)