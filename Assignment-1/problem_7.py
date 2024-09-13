# 7) Create a program that prints the Fibonacci sequence up to `n` terms, where `n` is provided by the user.

nterms=int(input("Enter a number : "))
n1,n2=0,1
count=0

list1=[]
# print(n1)
# print(n2)
list1.append(n1)
list1.append(n2)
while (count<nterms):
    count = n1 + n2
    if count< nterms:
        # print(count)
        n1=n2
        n2=count
        list1.append(count)
print(list1)