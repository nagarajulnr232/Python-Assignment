# Write a program that checks if a number is prime or not.
def check_prime(number):
    i, temp = 0, 0
    for i in range(2, number // 2):
        if number % i == 0:
            temp = 1
            break
    if temp == 1:
        print(number,"Is Not a Prime number")
    else:
        print(number,"Is Prime number")
number= int(input("Enter number : "))
check_prime(number)
