"""Lists are a type of Data Structure in Python.

1.  Most commonly used sequences.
2.  They are mutable: once they're created, the individual elements can
    be changed.
3.  To create a list, specificy comma separated values in between
    square brackets []. The values do not have to be of the same type.

    Example: my_list = ['tree', 'dog', 456, False]

4.  Each item on the list is assigned an index value, starting at zero.
    Remember that list item indexes start at zero.
    
Updating a List

1.  Create a list with random strings.
2.  Print the list.
3.  Get the length of the list.
4.  Get the 2nd item in the list.
5.  Get the 5th item in the list.
6.  You can add items to a list.
7.  Remove items from a list.
8.  Check if an item is in a list."""

list1 = ['1', 'dog', 'cat', '789'] #1
print(list1) #2
print(len(list1)) #3 (the number of items in a list)
print(list1[1]) #4 (index 1 inside of square brackets)
#5 print(list1[4])  Attemtps to get the 5th item on the list. However, this doesn't exist. "List index out of range."
list1.append("hello") #6
print(list1)
list1.pop() #7 Removes the last item in the list. A pop without index removes the last item on the list.
print(list1)
list1.pop(1) #7 Removes the second item in the list. A pop with specific item location.
print(list1)
print('dog' in list1)
"""even though dog is in original list, remember that you have since
edited the list to remove the second item."""

list2 = [1, 2, 3]
print(list2)
print(2 in list2)

"""

Types of Loops

1.  Loops are used to repeat a process (block of statements) or perform an operation
    multiple times.
2.  'for loops' run a piece of code for a given number of times.
3.  'while loops' run a piece of code indefinitely while a condition is met."""


print("New Section: For Loops")
"""
1.  To executing code a given number of times you can use a for loop and iterate over a list.
2.  Example:"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

"""Here, the 'for' line indicates we are passing through each element in the list once
(i.e., for each element in the list, do somethig). You indicate what you want it
to within an indented code block.

3.  In the 'for' line, we are referring to each item as "number" which is our
    dummy variable.
4.  We could have named this dummy anything (e.g., num, n, etc.).
5.  Our code runs through the enclosed code block 10 times."""
print('.')
print('.')
print('.')
print('.')
print('.')
print('.')

print("New Section: Iterating over a list")

"""
1.  We are going to iterative over the same list and find the numbers that are even.
2.  Define a list of numbers.
3.  Iterate over your list.
4.  Create a new, empty list (contains no items) to store even numbers.
5.  Use 'if' to test each number as you iterate through the list to see if it's even.
6.  If even, append the number to the empty list.
7.  Print the list of even numbers.
8.  We can also count the even numbers.
9.  Increment even_count.
10. You can also get the LENGTH of the even_numbers list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #2

even_numbers = [] #4

even_count = 0 #8 set your count to zero.

for x in numbers: #3
    if (x % 2 == 0): #5
        even_numbers.append(x) #6

        even_count += 1 #9 increments even_count by 1.
print(even_numbers)#7
print("There are" , even_count, "even numbers in the list.")
print("There are" , len(even_numbers) , "even numbers in the list.") #10

print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print("New Section: Finding the Minimum Value of a List of Numbers.")
"""
1.  Write code that finds the minimum value of a list of numbers 5, 3, 8, -1, -2.2, 0.
2.  Don't use the built-in min() function.
3.  Initiate a 'numbers' list variable containing the proper values (above).
4.  Define and keep track of the minimum number. Set the first minimum number as the first
    element of the list.
5.  Iterate over that list and find the min value.
6.  Print the minimum value in the format "...is the min number."""

numbers = [5, 3, 8, -1, -2.2, 0] #3
min_number = numbers[0] #4 min_number set as the first element of the list, 5
for x in numbers: #5, iterating over the list
    if x < min_number: #5, finding the minimum value by checking if each iteration is less than the min_number
      min_number = x #5if so, make that new iteration the min_number
print(min_number, "is the minimum number.") #6

print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print("New Section: Iterating Over Strings.")
"""
We can iterate over lists of strings.  """

planets = ["Sun", "Mercury", "Venus", "Earth", "Mars"]
for planet in planets:
    if (planet == "Sun"): #the parentheses are not required.
        print(planet, "is not a planet.")
    else:
        print (planet, "is a planet.")

    if planet == "Mercury":
        print(planet, "is closest to the sun.")

print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print("New Section: Iterating Over a String.")
"""
We can iterate over strings themselves.  """
month = "February"
print(month, "is spelled:")

for x in month: #iterates over each character in the string.
    print(x)

month = "March"
print(month, "is spelled:")

for x in month:
    print(x, end = ' ') #use the end parameter of the print function to print horizontally with a single space.


print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print("New Section: Iterating Over a Name.")
"""
1.  Prompt the user for their name.
2.  Using a for loop:
    Print each letter of the name (same line)
    Count each letter in the name.
3.  Print the count of letter in the name."""

name = input("Please enter your name: ")
letter_count = 0

print(name, "is spelled: ")
for x in name:
    print(x, end = ' ')
    letter_count += 1


print("") #prints an empty line
print(letter_count, "letters in the name", name)

print('.')
print('.')
print('.')
print('.')
print('.')
print('.')
print("New Section: for Loops Using range.")
"""
1.  The range function generates a sequesnce (range) of numbers
    This can be used like a list when you want to perform an action n number of times.
2.  Format: range(start, up_to, step)
    start and step are both optional
    up_to means 'up to but not including' the value
    Can only use integers (no floats)"""

print("Example of Using Range")

#Iterate over a sequence of 10 numbers, 0 - 9

for x in range(10): #x starts at 0 by default, and goes up to (but does not include) 10.
    print(x)
print("")

#Iterate over a sequence of 10 numbers, 0 - 9

for x in range(0, 10):
    print(x)
print("")

#Iterate over a sequence of 6 numbers, 1 - 6

for x in range(1, 7):
    print(x)
print("")

#Iterate over sequence of 5 numbers, 0 - 28, skipping every 6 numbers.

for x in range(0, 30, 7):
    print(x)
print("")

#Iterate over sequence of 6 numbers, counting backwards from 5 - 0.

for x in range(5, -1, -1):
    print(x)
print("")

#Find the numbers between 1 and 1200 that are odd

for x in range(1, 1201, x+2):
        print(x)
print("")

#OR it can be done like this:

odd_numbers = []

for number in range(1,1201):
    if (number % 2 != 0):
        odd_numbers.append(number)
print(odd_numbers)
print("")

#OR it can be done like this w/ count feature:

odd_numbers = []
odd_count = 0

for number in range(1,1201):
    if (number % 2 != 0):
        odd_numbers.append(number)

        odd_count += 1 
print(odd_numbers)
print("There are " , odd_count , "between 1 and 1200.")
print("")
