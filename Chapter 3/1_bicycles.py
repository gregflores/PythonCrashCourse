
#* A list is a collection of items in an order
# You can put anything you want into a list and they don't have to be related in any way
# naming convention is to make list names plural since they contain multiple items
# In Python square brackets [] indicate a list
# Items are seperated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Python prints list a representation including the square brackets

#* Accessing Elements in a List
# Lists are an ordered collection, so you can access any element in a list by telling Python the position or index of the item.
# To access an element, write the name of the list followed by the index of the item in square brackets

print(bicycles[0])

# This output is shown without quotes or square brackets
# This is more what you would want a user to see
# You can also use string methods on the string items in the list

print(bicycles[0].title())

#* Index Positions Start at 0, Not 1
# Python considers the first item in alist to be at Position 0, not 1
# To access the fourth item in a list, you request the item at index 3
print(bicycles[1])
print(bicycles[3])

# Python has special syntax for accessing the alst element in a list
# By asking for the item at index -1, Python always returns the last item in the list
print(bicycles[-1])

# This convention applies to other negative indexes as well.
# -2 will give you second from last, -3 third from last, etc.

#* Using Individual Values from a List
# You can use values from a list just as you would any other variable
messages = "My first bicycle was a " + bicycles[0].title() + "."
print(messages)