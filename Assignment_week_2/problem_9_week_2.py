''' Write a program that takes the lengths of the three sides of a triangle
    and determines if it's an equilateral, isosceles, or scalene triangle. '''

l1 = int(input("Enter first side l1: "))
l2 = int(input("Enter second side l2: "))
l3 = int(input("Enter third side l3: "))

if l1 == l2 and l2 == l3 :
    print("Equilateral Triangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")