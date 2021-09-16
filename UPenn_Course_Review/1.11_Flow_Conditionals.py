"""
if condition is True, execute statements in body of if,
elif (else if) another condition is True, execute statments in body of elif,
else (otherwise), execute statments in body of else"""

age = int(input("Enter age: "))
if age < 100:
    print("In" , 100 - age, "years you will be 100 years old.")
elif age == 100:
    print("You are" , age, "years old")
else:
    print("A century and going strong!")
