#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []
movie1 = input("Enter first movie: ")
movie2 = input("Enter second movie: ")
movie3 = input("Enter third movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#WAP to check if a list contains a palindrome of elements. [1,2,3,2,1]
list = [input("Enter the elements of the list: ")]
list2 = list.copy()
list2.reverse()
if(list2 == list):
    print(list,"contains a palindrome of elements")
else:
    print(list,"does not contain palindrome elements")

#WAP to count the number of students with the "A" grade in the following tuple. ["C","D","A","A","B","B","A"]
tuple = ("C","D","A","A","B","B","A")
count = tuple.count("A")
print(count)

#store the above values in a list and sort them from "A" to "D".
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)