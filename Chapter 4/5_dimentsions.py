
#* Tuples
#  Lists work well for storing sets of items that can change
#  throughout the life of a program The ability to modify lists is
#  particularly important when you're working with a list of users on a
#  websire or a list of characters ina  game However sometimes you'll
#  want to create a list of items that cannot change. Tuples allow you
#  to do just that. Python refers  to values that cannot change as
#  immutable, and an immutable list is called a tuple

#* Defining a Tuple
#  A Tuple looks just like a list except you use
#  parentheses instead of square brackets Once you define a tuple, you
#  can access individual elements by using each item's index, just as
#  you would for a list For example, if we have a rectangle that should
#  always be a certain size, we can ensure that its size doesn't change
#  by putting the dimentions into a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# We define the tuple dimensions using parentheses instead of square
# brackets We print each element in the tuple individually Let's see
# what happens if we try to change one of the items in the tuple
# dimensions = (200, 50) 
# #! dimensions[0] = 250 
# The code tries to change the value of the first dimension, but Python
# returns a type error. We are trying to alter a tuple, which can't be
# done to that type of object, Python tells us we can't assign a new
# value to an item in a tuple

#* Looping Through All Values in a Tuple
#  You can loop over all the values in a tuple using a for loop, just as
#  you did with a list
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#* Writing over a Tuple 
# Although you can't modify a tuple, you can assign a new value to a
#  variable that holds a tuple We can redefine the entire tuple
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModifed dimensions:")
for dimension in dimensions:
    print(dimension)
# We define the original tuple and prints the initial dimensions. We
# then store a new tuple in the variable dimensions and print. No errors
# because overwriting a variable is valid