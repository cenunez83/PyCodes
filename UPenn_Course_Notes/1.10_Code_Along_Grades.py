"""Prompt the user for a numerical grade and print the appropriate letter grade.

1. Get user input of a numberical grade.
2. Convert the user input to an integer.
3. Test the range of the number using flow control.
4. Print the appropriate letter grade."""

grade = int(input("What is your numerical grade?"))

if 90 <= grade <= 100: #if False, goes to next condition
    print("A")
elif 80 <= grade < 89: #if False, goes to next condition
    print("B")
elif 70 <= grade < 79: #if False, goes to next condition
    print("C")
elif 60 <= grade < 69: #if False, goes to next condition
    print("D")
else:
    print("F")

#OR

grade = int(input("Enter your grade: "))

if grade >= 90: #if False, goes to next condition
    print("A")
elif grade >= 80: #if False, goes to next condition
    print("B")
elif grade >= 70: #if False, goes to next condition
    print("C")
elif grade >= 60: #if False, goes to next condition
    print("D")
else: 
    print("F")
    
