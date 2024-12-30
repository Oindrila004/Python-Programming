marks = [89.8, 90, 76.9, 87, 56]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))

student =["Oindrila", 20, "Programmer"]
print(student)

# #slicing
print(marks[1:5])

#list methods
marks.append(67.8) #adds one element in the end
print(marks)

print(marks.sort()) #ascending order
print(marks)

print(marks.sort(reverse=True)) #Descending Order
print(marks)

marks.reverse() #Reverses the list
print(marks)

marks.insert(2, 67)
print(marks)