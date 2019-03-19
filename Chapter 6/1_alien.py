
#* Dictionaries
# Dictionaries allow you to connect pieces of related information. You'll learn how to access the information once it's in a dictionary and how to modify that information
# Because dictionaries can store an almost limitless amount of information, we will learn to loop through the data in a dictionary
# Learn to next dictionaries inside other dictionaries.
# Dictionaries allow you to model a variety of real-world objects more accurately
# You can create a dictionary about a person and then store as much info about them

#* A simple dictionary
alien_0 = {'color': 'green', 'points':5 }
print(alien_0['color'])
print(alien_0['points'])
# The dictionary store the alien's color and point value

#* Working with Dictionaries
# A dictionary in Python is a collection of key-value pairs
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A keys value can be a number, a string, a list, or even another dictionary
# In fact you can use any object that you can create in Python as a value in a dictionary
# In Python a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces
# A key-value pair is a set of values associated with each other
# when you provide a key, Python returns the value associated with that key
# Every key is connected to its value by a colon and key-pairs are separated by commas
alien_0 = {'color': 'green'}

#* Accessing Values in a Dictionary
# To get the associated value with a key, give the name of the dict and then place the key inside a set of square brackets
print(alien_0['color'])
# You can have an unlimited number of key-value pairs in a dict
alien_0 = {'color': 'green', 'points':5 }
# Now you can access either the color or the point value
# If a player shoots down this alien, you can look up how many points they should earn
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#* Adding New Key-Value Pairs
# Dicts are dynamic structures and you can add new pairs any time
alien_0 = {'color': 'green', 'points':5 }
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# We added a new key-value pair with 'x_position' and 'y_position'
# Python doesn't care about the order that the pairs are stored, only about the connection between key and value

#* Starting with an Empty Dictionary
# You can start with an empty dict and add pairs in their own line
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#* Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#* Removing Key-value pairs
# When you no longer need a piece of information that's stored in a dictionary, you can use the del statement to completely remove a key-value pair
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)