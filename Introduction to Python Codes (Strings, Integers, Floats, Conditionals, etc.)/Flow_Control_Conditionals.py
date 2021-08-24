#if...elif...else
"""allows us to make decisions and execute "code blocks" (groups of statements)
based on logical conditions"""

"""Code blocks are indented four spaces (single tab)."""

#"if" condition is True, execute statements in body of "if"
x = int(input("2 + 2 = "))
if x != 4:
    print("...try again") #Note the code block is indented by 4 spaces.

"""If condition is True, execute statements in body of if,
else (otherwise), execute statement in body of else."""
x = int(input("2 + 2 = "))
if x == 4:
    print("Correct") #body of if
else:
    print("...try again") #body of else (otherwise)


"""if condition is True, execute statements in body of if,
elif (else if) another condition is True, execute statements in body if elif,
else (otherwise), execute statements in body of else"""

age = int(input("Enter your age: "))
if age < 100:
    print("In", 100 - age, "years you will be 100 years old.")
elif age == 100:
    print("You are", age, "years old.")
else:
    print("A century and going strong!")

#You can have multiple elif conditions.

age = int(input("Enter your age: "))
if age = 0:
    print("Seriously?") #if age = 0, print this
elif age < 100:
    print("In", 100 - age, "years you will be 100 years old.") #otherwise, print this
elif age == 100:
    print("You are", age, "years old." #otherwise, print this
else:
    print("A century and going strong!") #otherwise, if none is true, print this

    


    
