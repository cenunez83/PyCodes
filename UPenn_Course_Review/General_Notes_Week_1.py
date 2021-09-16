"""Assigning a Variable 

You can increment a variable using += and decrement a variable using -+."""

#Example of Increment/Decrement 
 
x = 2
y = 3
print(x) 
print(y)

x = y 
y = x + 3
x += 1
y -= 1
print(x)
print(y)

"""Boolean Operators

There are three logical operators that are used to compare values, all of which
come down to true or false."""

#Example - AND Operator evaluates if two expressions are true or false.

x = 5
print(x > 3 and x < 5) #Prints False
print(3 < x < 5) #this is another way of printing the line above; also prints false.

#Example - OR Operator evaluates if at least one expression is true. 
y = 3
print(y < 3 or y == 3) #Prints True
print(y <= 3) #also prints true

#Example - NOT Operator returns the opposite of a value.
x = 6
y = 5
z = (y <= x)
print(not z) #prints the opposite of res, i.e., changes True to False or False to True. 

"""Variable Substitution

You can substitute variables in mathematical expressions"""

#Example

x = y = 10
z = 2 * x + y 
print(z) 

x = 42
b = 15 < (x / 2) < 25
print(b) #prints True
print(type(b)) #prints type boolean

x = 42
y = str(x)
x *= 2 #doubles the value of x (same as x = x * 2)
y *= 2 #doubles the value of y (same as y = y * 2)
print(x)
print(y)

"""Combining Variables"""

fav_movie = "Justin Bieber's 'Believe'"
fav_singer = "Justin Bieber"

favs = "Your favorite movie is " + fav_movie + " and your favorite singer is " + fav_singer
print(favs)

"""Getting User Input"""

fav_food = input('What\'s your favorite food?')
fav_movie = input('What\'s your favoriete movie?')

favorites = "Your favorite food is {} and your favorite movie is {}".format(fav_food, fav_movie)
#the {} are placeholders for the variables provided in the order in .format() field. 
print(favorites)


"""Flow Control: Conditionals 

if...elif...else allows us to make decisions and execute "code blocks" (groups of statements) based on logical conditions.
Code blocks are indented four spaces (a single tab). """

"""if a condition is True, execute statements in body of if"""

x = int(input("2 + 2 ="))
if x != 4:
    print("...try again!")

"""if a condition is True, execute statments in body of if, else (otherwise), execute statments in body of else."""
x = int(input("2 + 2 ="))
if x == 4:
    print("Correct!")
else:
    print("...try again")

"""if condition is True, execute statements in body of if,
elif (else if) another condition is True, execute statments in body of elif,
else (otherwise), execute statement in body of else."""

"""We can have multiple if conditions, where each condition is tested seperately

1. Ask the user to input an integer to evaluate
2. It is best practice to confirm entry is "numeric" before casting it to int"""

number = input("Enter an integer: ") #1

if (number.isnumeric()): #2 (we check using .isnumber()
    number = int(number)
    if (number > 20) : 
        print("Your integer: " + str(number) + " is greater than 20.")
    elif (number > 10) :
        print("Your integer: " + str(number) + " is greater than 10.")
    elif (number > 0) :
        print("Your integer: " + str(number) + " is greater than 0.")
else:
    print("Please input a valid entry.")

#note: .isnumeric() only works with positive integers.


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
    elif (number > 10) :
        print("Your integer: " + str(number) + " is greater than 10.")
    elif (number > 0) :
        print("Your integer: " + str(number) + " is greater than 0.")
except ValueError as e: #here, we don't really need the "else" clause
    print("Please input a valid entry.")



"""Functions

1. A function is a block of organized, reusable code that is used to perform a single, related action.
2. A function provides better modularity for your applications and a high degree of code reusing.

Python has built-in functions that are part of the core language, but it also allows you to define 
your own user-defined functions.

For reference: https://docs.python.org/3/library/functions.html"""

"""User-Defined Functions

1. Functions have conventions:
    a. name a function based on what it does.
    b. whitespace is important (function body 'code blocks' (groups of statements) have to be indented
    (4 spaces or tab).

2. Sometimes a function takes an input:
    a. These are called parameters.
    b. When you call (use) a function, you pass arguments to satisfy the parameters.

3. Sometimes a function produces an output:
    a. This is called the function's return value
    
You define a function using the def keyword, followed by the function name and parentheses

def function_name(param1, ..., paramN):
    statements
    return

The parantheses include optional parameters, treating them as variables.
Functions optionally return a value, which allows us to get the value out of the function after
it's done executing. Whatever follows the return keyword will be sent back to the location in your 
code where the function was called.

Example:
1. Let's define a function say_hello
2. It has no parameters, which means there is nothing passed to the function when it is called"""

def say_hello(): #1
    print("Hello!") #2
#Here's how we use the function say_hello
say_hello() #this will result in "Hello!"


"""Example:
1. Define a function say_something_specific
    a. It takes one string as a parameter.
    b. It prints that given string."""

def say_something_specific(a): #a
    print(a) #b

say_something_specific("Hello, again!")

"""Example:"""

def number_sum(num1, num2): #we are creating our function with its parameters
    sum = num1 + num2 #we tell the function what to do with the arguments that satisfy the parameters (then store in a variable 'sum'). 
    print("The sum is:" , sum) 
    return sum #we are also asking the function to return (print) the output (8). 

a = 5
b = 3
result = number_sum(5, 3) #we have called the function, and pass 5 and 3 in as arguments, and store as the variable "result"
print(result) #we then print the variable 
#This will print:
""" The sum is 8"
    8               """ 

"""Example using 'grade code along' exercise:"""

def numeric_grade_to_letter_grade (grade):
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

grade = int(input("Enter numeric grade: "))
numeric_grade_to_letter_grade(grade)

