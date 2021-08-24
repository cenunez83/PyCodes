#Here is an even better way to check for an integer (as opposed to isnumeric).

number = input("Please input an integer.")
#Try to cast the input
try:
    number = int(number)
#Catch the raised exception if there is an error - i.e., it can't be casted.
except ValueError as e:
    print("Your input is not an integer.")
    print(e) #You can also access/print the exception's message
#Otherwise, there is no error - i.e. the input was casted
else:
    print(str(number) + " is indeed an integer!")

#You can do the following w/ try/except instead

"""number = (input("Enter Number: "))
if (number.isnumeric()): 
    number = int(number) 
    if number > 20:
        print("Your input: " + str(number) + " > 20")
    if number > 10:
        print("Your input: " + str(number) + " > 10")
    if number > 0:
        print("Your input: " + str(number) + " > 0")
    if number < 0:
        print("Your input: " + str(number) + " is negative")
else:

    print("Your input is not an integer or it's negative.")"""


number = (input("Enter Number: "))
try:
    number = int(number) 
    if number > 20:
        print("Your input: " + str(number) + " > 20")
    if number > 10:
        print("Your input: " + str(number) + " > 10")
    if number > 0:
        print("Your input: " + str(number) + " > 0")
    if number < 0:
        print("Your input: " + str(number) + " is negative")
except ValueError as e:
    print("Your input is not an integer.")
    print(e)

    
