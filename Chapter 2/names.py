
#* Strings continued
#* Changing Case in a String with Methods

name = "ada lovelace"
print(name.title())

# name is a variable
# title() is a method
# A method is an action that python can perform on a piece of data
# The dot (.) in name.title() tells Python to perform the title() method on the variable name
# title() displays each word in titlecase, where each word begins with a capital letter
# Useful for names because you will want the program to interpret ada, ADA, and Ada, as the same name
# Then display the name as Ada

# There are several methods available that deal with case

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# The lower() method is useful for storing data.
# Many time you won't trust the users capitalization.
# You will lowercase all inputs before storing
# Then you will use whatever case makes sense before displaying

#* Combining or Concatenating Strings
# It is often useful to combine strings
# You may want to store a first and last name in seperate variables then combine them for display

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# Python uses the '+' symbol to combine strings
# This method of combining strings is called concatenation

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

