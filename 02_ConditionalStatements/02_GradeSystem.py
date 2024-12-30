marks = float(input("Enter your marks here: "))
if(marks >= 90):
    print("Your grade is A")
elif(90 > marks >= 80):
    print("Your grade is B")
elif(marks >= 70 and marks < 80): #and operator used
    print("Your grade is C")
elif(0 < marks < 70):
    print("Your grade is D")
else:
    print("Invalid Input")