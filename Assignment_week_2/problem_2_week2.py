#  Implement a program that prints the multiplication table of a number provided by the user.

def tables(number):
    for i in range(1,11):
        result=i*number
        print(f"{number}*{i}={result}")
number=int(input("Enter number for the multiplication table of a number : "))
tables(number)