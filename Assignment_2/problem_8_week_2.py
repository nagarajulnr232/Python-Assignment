## Create a program that calculates the sum of the digits of a number.

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = int(input("Enter Number: "))
print(getSum(n))


######################################################

def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10

    return sum


n = int(input("Enter Number: "))
print(getSum(n))



