#Write a program to input 2 numbers & print their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print(sum)

#WAP to input side of a square and print its area
side = float(input("Enter the side of the square: "))
area = side ** 2
print(area)

#WAP to input 2 floating point numbers and print their average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2)/2
print(average)

#WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(not (num1 < num2))