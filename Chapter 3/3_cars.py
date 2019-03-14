
#* Organizing a List
# Often your lists will be created in an unpredictable order
# You will often want to present your data in a predictable order
# Python provides a number of ways to organize your lists

#* Sorting a list permanently with the sort() Method
# Pythons sort() method makes it relatively easy to sort a list
# Lets sort a list alphabetically. Assume all lowercase
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# The sort() method changes the order of the list permanently
# We will not be able to revert the order

# The list can aldo be sorted in reverse alpha order by passing the argument reverse=True to the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Again this permanently changes the order

#* Sorting a List Temporarily with the sorted() function
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function
# This lets you display your list in a particular order, but doesn't affest the actual order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# The sorted function can also accept a reverse=True argument

# Sorting when all values are not lowercase is more complex

#* Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# The reverse method changes the order of a list permanently but can be reverted using the reverse() method again

#* Finding the length of a List
# You can quickly find the length of a list by using the len() function. The list in this example has four items, so its length is 4
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#LEFT ON PAGE 50