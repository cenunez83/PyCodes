"""ORGRANIZING LISTS"""

#Sorting a list permanently with sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
"""the list is changed permanently, and we can never revert to the original order"""

#you can also sort a list in reverse alphabetical order (still permanently)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#you can temporarily sort a list using sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the orginal list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\nHere is the original list again: ")
print(cars)

#printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#Notice that it doesn't sort in reverse alphabetical order, just in reverse order.
#reverse() changes permanently, but you can revert to original by reversing again.

#Finding the Length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)