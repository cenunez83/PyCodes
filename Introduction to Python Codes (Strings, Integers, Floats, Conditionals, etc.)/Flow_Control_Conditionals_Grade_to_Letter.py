"""Prompt the user for a numerical grade and print the appropriate
letter grade.

1. Get user input of a numerical grade.
2. Convert the input to an integer.
3. Test the range of the number using flow control.
4. Print the appropriate letter grade. For example, if the user enters a number
between 90 - 100, give them an 'A'."""

grade = int(input("Enter Numerical Grade: "))
if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
elif grade <= 59:
    print("F")

#You can also do it as follows:

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

#Multiple if conditionals w/ user error check using isnumberic method:

number = (input("Enter Number: "))
if (number.isnumeric()): #checks if all inputs are numberic/digits
    number = int(number) #if so, then cast the input as int
    if number > 20:
        print("Your input: " + str(number) + " > 20")
    if number > 10:
        print("Your input: " + str(number) + " > 10")
    if number > 0:
        print("Your input: " + str(number) + " > 0")
else:
    print("Your input is not an integer or it's negative.")

#Note: isnumeric only works with positive integers.
