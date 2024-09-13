# 2) Create a program that takes two numbers from the user and prints their sum.

x=int(input("Enter num1: "))
y=int(input("Enter num2: "))
c=x+y
print("Sum ofsum1 & num2 :",c)

##using another method

def sum(num1,num2):
    return num1+num2
result=sum(50,60)
print("Sum of num1 and num2:",result)

# ##using another method

class sum:
    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y
    def display(self):
        total =self.num1+self.num2
        print("Sum of two numbers num1 & num2:", total)
add_number=sum(49,50)
add_number.display()
