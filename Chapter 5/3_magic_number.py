
#* Numerical Comparison
# The following code checks whether a person is 18 yeats old
age = 18
print(age == 18)

# You can also test to see if two numbers are not equal
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
# The conditional test passes because the value of answer is not equal to 42. Because the test passes, the indented code block is executed
# You can include various mathematical comparisons in you conditional statements as well
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#* Check Multiple Conditions
# You may want to check multiple conditions at the same time.
# The keywords and and or can help you

#* Using and to Check Multiple Conditions
# To check whether two conditions are both True simultaneously, use the keyword and to combine the to conditional tests
age_0 = 22
age_1 = 18
print( age_0 >= 21 and age_1 >= 21)
age_1 = 22
print( age_0 >= 21 and age_1 >= 21)
# We defind two ages and we check whether both ages are 21 or older. The first test passes but the second test fails
# We then change age_1 to be greater than 21, and now both tests pass and the expression evaluates to True

#* Using or to Check Multiple Conditions
# The keyword or allows you to check multiple conditions as well, but it will pass when either or both tests pass
# The or expression only fails when both tests fail
age_0 = 22
age_1 = 18
print( age_0 >= 21 or age_1 >= 21)
age_0 = 18
print( age_0 >= 21 and age_1 >= 21)
# We start with two variables and pass the test because age_0 is greater than 21, after changing age_0 to 18 neither test passes so the entire expression fails

#* Checking Whether a Value Is in a List
# You may want to check whether a list contains a certain value
# To find whether a value is in a list, use the keyword in.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print( 'mushrooms' in requested_toppings) #TRUE
print( 'pepperoni' in requested_toppings) #FALSE
