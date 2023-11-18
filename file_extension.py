import os

'''Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''

os.system("cls")

file_name = input("Enter the full file name:\t")

ext = file_name.split(".")

print("\n."+ext[1], "\n")

