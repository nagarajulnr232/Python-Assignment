## Create a program that calculates the sum of the digits of a number.

def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a number: "))
print("The sum of the digits is:", sum_of_digits(number))



