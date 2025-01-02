#WAP to find the sum of first n numbers. (using while)
n = int(input("Enter n:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)

#WAP to find the factorial of first n numbers.(using for)
n = int(input("Enter n: "))
fact = 1
for i in range(1, (n+1)):
    fact *= i
print(fact)