
#* Checking Whether a Value Is Not in a List
# You can use the keyword not in this situation
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# The expression checks if the user is not in the list of banned_users
# The return is True and executes the indented line

#* Boolean Expressions
# As you learn more about programming, you'll hear the term boolean expression at some point.
# A boolean expression is just another name for a conditional test.
# A boolean value is either True or False
# Boolean values are used to keep track of certain conditions
game_active = True
can_edit = False
