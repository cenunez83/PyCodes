bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#access element in a list
print(bicycles[0])
print(bicycles[0].title())

#use [-1] to access the last element of any list.
print(bicycles[-1].title())

#using individual values from a list
"""you can use individual items from a list just as you would any variable."""

message = f"My first bicycle was a {bicycles[0].title()}. I loved it!"
print(message)

#modifing elements in a list

#changing an element on a list
attendees = ['sam', 'luke', 'timothy', 'librarian']
print(attendees)
attendees[-1] = 'bob'
print(attendees)

#adding elements to a list by using append()
attendees = ['sam', 'luke', 'timothy', 'librarian']
print(attendees)
attendees.append('billy')
print(attendees)

#adding elements to an empty list by using append()
goals = []

goals.append('learn languages')
goals.append('finances')
goals.append('get into grad school')
goals.append('find your faith')
print(goals)

#inserting elements in a specific position using insert()
tasks = ['in progress', 'complete', 'not started']
tasks.insert(1, 'waiting on requester')
print(tasks)

#removing elements from a list using del
genres = ['fiction', 'nonfiction', 'country'] 
del genres[2]
print(genres)

#removing elements using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

meals = ['breakfast', 'lunch', 'dinner']
last_meal = meals.pop()
print(f"The last meal I had today was {last_meal}.")

#popping at a specific position
meals = ['breakfast', 'lunch', 'dinner']
missed_meal = meals.pop(1)
print(f"I usually have three meals a day. But today I didn't have {missed_meal}.")

#removing an item by value
meals = ['breakfast', 'lunch', 'dinner']
meals.remove('dinner')
print(meals)
#remove() only removes the first occurrence of the specified value