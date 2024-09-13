# 3)Write a program that calculates the area of a rectangle given its length and width.

length=int(input("Enter length of the rectangle: "))
width=int(input("Enter width of the rectangle: "))
Area_rectangle=length*width
print(Area_rectangle)

# ## Using Another method

def area_rectangle(length,width):
    return length*width
area=area_rectangle(40,60)
print("Area of the rectangle:",area)

# ## Using Another method

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        area_rectangle=self.length*self.width
        print("Length of the rectangle:",self.length)
        print("Width of the rectangle:",self.width)
        print("Area of the rectangle:",area_rectangle)
area=Rectangle(60,80)
area.display()