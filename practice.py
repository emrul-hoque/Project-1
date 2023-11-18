import sys


'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

mylist = []
mytuple = ()

for i in range(5):
    x = input("Enter first number:\t")
    mylist.append(x)
    mytuple += (x, )

print(mylist)
print(mytuple)