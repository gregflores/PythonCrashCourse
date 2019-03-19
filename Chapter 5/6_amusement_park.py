# if-else Statements
# Often you'll want to take one action when conditional test passes and a different action in all other cases
# if-else syntax makes this possible
# An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18!")

#* The if-elif-else chain
# You'll often need to test more than two possible situations
# Using an if-elif-else syntax, python will execute only one block in the chain.
# It runs each conditional test in order until one passes, when a test passes, the code in that block is executed and the rest is skipped
age = 12
if age < 4:
    print('Your admission cost is $0')
elif age <18:
    print('Your admission cost is $5')
else:
    print('Your admission cost is $10')
# The test checks where you fit into the age bracket
# Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the chain
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#* Using Multiple elif Blocks
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#* Omitting the else block
# Python does not need the else block at the end of an if-elif chain
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# The else block is a catchall statement
# It matches any condition that wasn't matched by a specific if or elif test