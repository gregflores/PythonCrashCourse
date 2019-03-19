
#* If statements
# When you understand conditional tests, you can start writing if statements
# Several different kinds of if statements exist, and your choice of which to use depends on the numbers of conditions you need to test

#* Simple if statements
# The simplest kind of if statement has one test and one action
#if conditional_test:
#    do something
# You can put any conditional test in the first line and just about any action in the indented block following the test
# If the conditional test evaluates to True,Python executes the code following the if statement, false ignores the code following
age = 19
if age >= 18:
    print("You are old enough to vote!")
# Python checks if age is greater than or equal to 18
# Indentation plays the same role in if statements as it did in for loops.
# All indented lines after an if statement will be executed if the test passes
# You can have as many lines of code as you want in the block following the if statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

