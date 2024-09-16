## Write a program that takes a list of numbers and finds the largest number in the list.

list1=[13,23,24,14,19,61,82]
print("The largest number is" ,max(list1))

## Another method

largest_number=sorted(list1)
print("The largest number is",largest_number[-1])

## Another method

def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max

list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))