# Create a program that calculates the sum of all natural numbers up to `n` using a loop.

num = int(input("Enter number: "))
sum = 0
for i in range(num+1):
  sum+=i
print(f"Sum of all natural numbers up to {num} is {sum}")