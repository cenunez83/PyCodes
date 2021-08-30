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

