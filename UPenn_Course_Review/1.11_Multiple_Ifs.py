"""We can have multiple if conditions, where each condition is tested seperately

1. Ask the user to input an integer to evaluate
2. It is best practice to confirm entry is "numeric" before casting it to int"""

number = input("Enter an integer: ") #1

if (number.isnumeric()): #2 (we check using .isnumber()
    number = int(number)
    if (number > 20) : 
        print("Your integer: " + str(number) + " is greater than 20.")
    if (number > 10) :
        print("Your integer: " + str(number) + " is greater than 10.")
    if (number > 0) :
        print("Your integer: " + str(number) + " is greater than 0.")
else:
    print("Please input a valid entry.")

#note: .isnumeric() only works with positive integers.
#note: multiple if statements is essentially using elif. 


"""An even beter way to catch an error is to use a "try block" """

number = input("Enter a positive integer: ")

try: #try to cast the input
    number = int(number)
except ValueError as e: #catch the raised exception if there is an error (i.e., it cannot be cast)
    print("Your entry, " + str(number) + ", is not an integer.")
    print(e) #you can access/print the exception's message
else: #otherwise, there is no error (i.e., the input was successfully casted)
    print(str(number) + " is indeed an integer!")


"""Another example"""

number = input("Enter an integer: ") #1
try:
    number = int(number)
    if (number > 20) : 
        print("Your integer: " + str(number) + " is greater than 20.")
    if (number > 10) :
        print("Your integer: " + str(number) + " is greater than 10.")
    if (number > 0) :
        print("Your integer: " + str(number) + " is greater than 0.")
except ValueError as e: #here, we don't really need the "else" clause
    print("Please input a valid entry.")