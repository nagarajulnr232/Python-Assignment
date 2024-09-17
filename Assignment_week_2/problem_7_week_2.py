## Write a program that takes a list of numbers and separates them into even and odd lists.

def split_even_odd(value):
    even=[]
    odd=[]
    for i in value:
        if (i%2 == 0):
            even.append(i)
        else:
            odd.append(i)
    print("Main List:",value)
    print("After separates even and odd lists")
    print("Even list:",even)
    print("Odd list:",odd)

value=[12,14,13,11,45,38,71,62]
split_even_odd(value)



