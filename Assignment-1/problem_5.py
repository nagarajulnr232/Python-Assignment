# 5) Implement a program that calculates the factorial of a number using a loop.

def facorial(number):
    res=1
    for i in range(1,number+1):
        res *= i
    return res
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative number")
else :
    print(f"The factorial {number} is {facorial(number)}.")