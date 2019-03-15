
#* If Statements
#  Programming often involves examining a set of conditions and deciding
#  which action to take based on those conditions. Python's if statement
#  allows you to examine the current state of a program and respoond
#  appropriately to that state.
#  In this chapter you'll learn to write conditional tests, which allow
#  you to check any condition of interest. You'll write simple if
#  statements then use more complex series of if statements to identify
#  when the conditions you want are present. You'll then apply this
#  concept to lists, so you'll be able to write a for loop that handles
#  most items in a list one way but handles certain items with specific
#  values in a different way.

#* A Simple Example
#  The following short example shows how if tests let you respond to
#  special situations correctly. Imagine you have a list of cars and you
#  want to print out the name of each car. Car names are proper names,
#  so the names of most cars should be printed in title case. However,
#  'bmw' should be printed all uppercase. The code loops through the
#  list of cars and looks for 'bmw' and prints it uppercase
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# The loop in this example first checks if the current value of cars is
# 'bmw'. If it is, the value is printed in uppercase. If the value of
# car is anything other than 'bmw', it's printed in title case.

#* Conditional Tests
#  At the heart of every if statement is an expression that can be
#  evaluated as True or False and is called a condition test. Python
#  uses the True and False to decide whether the code in an if statement
#  should be executed. If a test evaluates to True, Python executes the
#  following code. False means it ignores the following code.

#* Checking for Equality
#  Most conditional tests compare the current value of a var to a
#  specific value of interest. The simplest conditional test checks
#  whether the value of a var is equal to the value of interest
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
# The value of car is set to 'bmw' using a single equal (=) sign. The
# next line checks whethere the value of car is 'bmw' using a double
# equal (==) sign. This equality operator returns True if the values on
# the left and right side of the operator match, and false if they don't
# match. A single equal sign is really a statement "Set the value of car
# equal to 'audi'". On the other hand, a double equal sign asks a
# question, "Is the value of car equal to 'bmw'?"

#* Ignoring Case When Checking for Equality
#  Testing for equality is case sensitive in Python. Two values with
#  different capitalization are not considered equal
car = 'Audi'
print(car == 'audi')
# If case matters, this is advantageous. If case doesn't matter and
# instead you just want to test the value of a variable, you can convert
# the variable's value to lowercase before doing the comparison
car = 'Audi'
print(car.lower() == 'audi')
# This test would return True no matter how the value 'Audi' is
# formatted because the test is now case insensitive. The lower()
# function doesn't change the value that was originally stored in car,
# so you can do this kind of comparision without affecting the original
# variable
car = 'Audi'
print(car.lower() == 'audi')
print(car)
# We store the capitalized string 'Audi' in the variable car. We convert
# the value of car to lowercase and compare the lowercase value to the
# string 'audi'. The two strings match. So Python returns True. We print
# car and see that value hasn't been changed.