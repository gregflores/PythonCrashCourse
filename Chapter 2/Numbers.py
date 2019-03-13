
#* Integers
# You can add (+), subtract(-), multiply(*), and divide(/)
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# Python uses two multiplication symbols to represent exponents
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

#Python supports order of operations so you can use multiple operations in one expression. Parentheses can be used to modify the order of operations to be interpreted in the order you specify.
print(2 + 3 * 4)
print((2 + 3) * 4)

#* Floats
# Python calls nay number with a decimal point a float. This term refers to the fact that the decimal point can appear at any position.
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

# Be aware that you can sometimes get an arbitrary number of decimal places in your answer
print(0.2 + 0.1)
print(3 * 0.1)

# This happens in all languages and is of little concern. Ignore the extra decimal places for now. You will learn ways to deal with the extra places when you need to in the projects in Part II

#* Avoiding Type errors with the str() function
# Often you will want to use a vars value within a message
#! age = 23
#! message = "Happy" + age + "rd Birthday"
#! print(message)
# You might expect this code to print the greeting. Instead you will get a type error. 
# Type errors mean Python can't recognize the kind of information you're using. Using the integer value could be interpreted as the numerical value 23 or the characters 2 and 3. When using integers within strings like this, you need to specify that you want Python to use the integer as a string of characters. You can do this by wrapping the var in the str() function.
age = 23
message = "Happy" + str(age) + "rd Birthday"
print(message)


