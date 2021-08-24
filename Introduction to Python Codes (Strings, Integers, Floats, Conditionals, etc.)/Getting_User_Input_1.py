fav_movie = input("What is your favorite movie? ")
fav_singer = input("Who is your favorite singer? ")

favs = "Your favorite movie is " + fav_movie + "." + " And your favorite singer is " + fav_singer + "."
print(favs)

favs1 = "Your favorite movie is {}. And your favorite singer is {}.".format(fav_movie, fav_singer)
print(favs1)
"""Function str.format() works by putting in one or more replacement fields
and placeholders defined by a pair of curly braces {} into a string and calling the str.format().
The value we wish to put into the placeholders and concatenate with the string passed as parameters
into the format function."""

"""For example:
str = "This code is written in {}"
str1 = str.format("Python!")
print(str1)
Now, the str1 will be like 'This code is written in Python!'"""

age = int(input("How old are you? "))
print(age + 3)

str = "This code is written in {}".format("Python!")
print(str)

str2 = "My name is {}"
str3 = str2.format("Peter!")
print(str3)
str4 = "This code is written in {}".format(str3)
print(str4)

