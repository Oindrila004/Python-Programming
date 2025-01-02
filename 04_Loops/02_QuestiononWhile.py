#Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

#Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

#Print the multiplication table of a number n
n = int(input("Enter your number: "))
i = 1
while i <= 10:
    print(n, "*", i , "=", n*i)
    i += 1

#Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#Search for a number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter number to search: "))
nums = (1,4,9,16,25,36,49,64,81,100)
idx = 0
while idx < len(nums):
    if (nums[idx] == x):
        print(x, "number found at index", idx)
    idx += 1