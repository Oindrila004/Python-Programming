#WAP to check if a number entered by the user is odd or even
number = int(input("Enter a number to check: "))
if(number % 2 == 0):
    print(number,"is even")
elif(number % 2 != 0):
    print(number,"is odd")
else:
    print("Invalid input")

#WAP to find the greatest of 3 numbers entered by the user
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))
if(number1 > number2 and number1 > number3):
    print(number1,"is the greatest")
elif(number2 > number3):
    print(number2,"is the greatest")
else:
    print(number3,"is the greatest")

#WAP to check if a number is a multiple of 7 or not
number = int(input("Enter a number: "))
if(number % 7 == 0):
    print(number,"is a multiple of 7")
else:
    print(number,"is not a multiple of 7")