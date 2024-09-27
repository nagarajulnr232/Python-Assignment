#  Write a program that takes a score from the user and returns the corresponding letter grade (A, B, C, D, F).

def grade_wise(score):
    if score>=60:
        print("Grade: A")
    elif score <59.99 and score >=50:
        print("Grade: B")
    elif score<49.99 and score>=35:
        print("Grade: C")
    else:
        print("Fail")
score=int(input("Enter Marks: "))
grade_wise(score)