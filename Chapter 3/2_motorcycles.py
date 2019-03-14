
#* Changing, Adding, and Removing Elements
# Most lists you create will be dynamic, meaning you will build a list and add and remove elements

#* Modifying Elements in a List
# Modifying an element is similar to the syntax for accessing an element in a list.
# To change an element, use the name of the list and the index then provide the new value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#* Adding elements to a list
# Python provides several ways to add new data to existing lists
# the simplest way to add a new element to a list is to append the item to a list
# Appending adds the item to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# The append() method make it easy to build lists dynamically
# You can start with an empty list and add items using append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#* Inserting elements into a list
# You can add a new element at any position by using the insert() method
# Specify the index and the value of the new element
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# In this example, ducati is inserted at position 0 and all other values are shifted one position to the right

#* Removing Elements from a list
# Often you'll want to remove an item or a set of items from a list
# You can remove an item according to its position or according to its value
# If you know the position you can use the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# del was used to remove the first item from the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# del can be used to delete an item from any position

#* Removing an item using the pop() method
# Sometimes you'll want to use the value of an item after you remove it from a list
# The pop() method removes the last item in a list, but lets you work with that item after removing it
# The term pop comes from thinking of a list as a stack of items and popping items off the top of the stack
# In the this analogy the top of a stack corresponds to the end of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We pop a value from the list and store the value in a var
# We print the list to show the item has been removed
# Then we print the value to show we still have access to the value

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#* Popping Items from any position in a list
# You can use pop() to remove an item in a list from any position by including the index
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The last motorcycle I owned was a " + first_owned.title() + ".")

# Remember that each time you use pop(), the item is no longer stored in the list

#* Removing an Item by Value
# Sometime you won't know the position of the value you want to remove from a list. If you only know the value of the item to remove, you can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that being removed from a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# The remove() methods only deletes the first occurence of the value
# If there's a possibility the value appears more than once in the list, you'll need to use a loop to determine if all occurrences of the value have been removed