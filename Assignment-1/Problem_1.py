# 1) Print Your Name: Write a program that prints your name to the console.
#
# Name=input("Enter your name: ")
# print(Name)
#
# 2) Create a program that takes two numbers from the user and prints their sum.
#
# x=int(input("Enter num1: "))
# y=int(input("Enter num2: "))
# c=x+y
# print("Sum ofsum1 & num2 :",c)
#
# ##using another method
#
# def sum(num1,num2):
#     return num1+num2
# result=sum(50,60)
# print("Sum of num1 and num2:",result)
#
# ##using another method
#
# class sum:
#     def __init__(self,x,y):
#         self.num1 = x
#         self.num2 = y
#     def display(self):
#         total =self.num1+self.num2
#         print("Sum of two numbers num1 & num2:", total)
# add_number=sum(49,50)
# add_number.display()
#
# 3)Write a program that calculates the area of a rectangle given its length and width.
#
# length=int(input("Enter length of the rectangle: "))
# width=int(input("Enter width of the rectangle: "))
# Area_rectangle=length*width
# print(Area_rectangle)
#
# ## Using Another method
#
# def area_rectangle(length,width):
#     return length*width
# area=area_rectangle(40,60)
# print("Area of the rectangle:",area)
#
# ## Using Another method
#
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def display(self):
#         area_rectangle=self.length*self.width
#         print("Length of the rectangle:",self.length)
#         print("Width of the rectangle:",self.width)
#         print("Area of the rectangle:",area_rectangle)
# area=Rectangle(60,80)
# area.display()
#
# 4) Write a program that checks whether a number entered by the user is odd or even.
#
# num=int(input("Enter number: "))
# if num%2== 0:
#     print("Entered number is Even!")
# else:
#     print("Entered number is Odd")

# 5) Implement a program that calculates the factorial of a number using a loop.

# def facorial(number):
#     res=1
#     for i in range(1,number+1):
#         res *= i
#     return res
# number = int(input("Enter a number: "))
# if number < 0:
#     print("Factorial is not defined for negative number")
# else :
#     print(f"The factorial {number} is {facorial(number)}.")

# 6) Write a program that checks if a given string is a palindrome

# def is_palindrome(string):
#     return string==string[::-1]
# string=input("Enter any word : ")
# pal=is_palindrome(string)
# if pal:
#     print("Is palindrome")
# else:
#     print("Not palindrome")

# 7) Create a program that prints the Fibonacci sequence up to `n` terms, where `n` is provided by the user.

# nterms=int(input("Enter a number : "))
# n1,n2=0,1
# count=0
#
# list1=[]
# # print(n1)
# # print(n2)
# list1.append(n1)
# list1.append(n2)
# while (count<nterms):
#     count = n1 + n2
#     if count< nterms:
#         # print(count)
#         n1=n2
#         n2=count
#         list1.append(count)
# print(list1)

# 8) Write a program that counts the number of vowels in a user-provided string.