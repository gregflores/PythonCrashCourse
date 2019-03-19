
#* Checking for Inequality
#  When you want to determine whether two values are not equal, you can
#  combine an exclamation point and an equal sign (!=). The exclamation
#  point represents not. Let's use another if statement to examine how
#  to use the inequality operator. 
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#  The if statement compares the value of requested_topping to the value
#  'anchovies'. If these two values do not match, Python returns True
#  and executes the code following the if statement. 

#* Using if Statements with Lists
# You can do some interesting work when you combine lists and if statements
# You can watch for special values that need to be treated differently than other values in the list

#* Checking for Special Items
requested_toppings = ['muschrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# What if the pizzeria runs out of green peppers?
requested_toppings = ['muschrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#* Checking That a List Is Not Empty
# We have assumed about every list has at least one item.
# Once the users start giving input we can't assume that
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza")
else:
    print("\nAre you sure you want a plain pizza?")

#* Using Multiple Lists
# Let's watch out for unusual topping requests before we build a pizza.
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")