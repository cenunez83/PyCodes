#Creating a function to convert numerical grade to letter grade
def numeric_to_letter_grade():
    grade = int(input("Enter Numerical Grade: "))
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

#call the numeric_to_letter_grade function defined above
numeric_to_letter_grade()

"""or we can do the following:"""

def numeric_to_letter_grade(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

#call the numeric_to_letter_grade function defined above w/ an argument to assess
numeric_to_letter_grade(87)

"""or we can do the following:"""

def numeric_to_letter_grade(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

#get user input of a numeric grade
grade = int(input("Enter Grade: "))
#call the numeric_to_letter_grade function defined above
numeric_to_letter_grade(grade)
