# 9) Create a program that takes a string as input and returns the reversed string.

def reverse(string):
    rev_string=string[::-1]
    return rev_string
string=input("Enter the string : ")
print("Reversed string :",reverse(string))