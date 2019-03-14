
#* Making numerical lists
# Lists are ideal for storing sets of numbers and Python provides a number of tools to help you work efficiently with lists of numbers.

#* Using the range() function
# Python's range() function makes it easy to generate a series of numbers
for value in range(1,5):
    print(value)
# This code prints the numbers 1-4
# This is a result of the off-by-one behavior
# The range() function causes Python to start counting at the first value you give it and stops when it reaches the second value you provide
# Because it stops at the second value, the output never contains the end value which is 5 in this case
for value in range(1,6):
    print(value)

#* Using range() to Make a List of Numbers
# To make a list of numbers, you can convert the results of range() to a list using the list() funcion
numbers = list(range(1,6))
print(numbers)

# We can also use the range() function to tell Python to skip to numbers in a given range
even_numbers = list(range(2,11,2))
print(even_numbers)
# In this example we start at the value 2, then add 2 to the value until it reaches or passes the end value, 11

# You can create almost any set of numbers you want using the range() function.
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
# This code can be rewritten as
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#* Simple Statistics with a List of numbers
# You can easily find the minimum maximum and sum of a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#* List Comprehensions
# The approach above generated the list squares consisted of using three or four lines of code.
# A list comprehension allows you to generate this same list in just one line of code
# A list comprehension combines the for loop and the creation of new elements into one line and automatically append each new element
squares = [value**2 for value in range(1,11)]
print(squares)