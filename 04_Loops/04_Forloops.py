list = [1,2,3,4,5]
for val in list:
    print(val)
else:
    print("End")

#Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in list:
    print(val)

#Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter number: "))
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
idx = 0
for val in tup:
    if (x == val):
        print(x, "FOUND at index", idx)
        break
    idx += 1