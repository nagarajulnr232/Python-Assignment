# 8) Write a program that counts the number of vowels in a user-provided string.

string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)

# ## Another Method

string=input("Enter string: ")
vowels="aeiouAEIOU"
count=sum(string.count(vowel) for vowel in vowels )
print("The number of vowels in entered string is :",count)

# ## Another method

string=input("Enter string : ")
vowels="aeiouAEIOU"
count =0
for a in vowels:
    counter = string.count(a)
    count = count + counter

print(count)