# 6) Write a program that checks if a given string is a palindrome

def is_palindrome(string):
    return string==string[::-1]
string=input("Enter any word : ")
pal=is_palindrome(string)
if pal:
    print("Is palindrome")
else:
    print("Not palindrome")