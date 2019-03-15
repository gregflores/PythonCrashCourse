
#! Page 65
# * Working with Part of a List
# We've learned how to work with individual elements of a list and how to work through all the elements in a list
# You can also work with a specific group of items in a list, called a slice

#* Slicing a List
# To make a slice, you specify the index of the first and last elements you want to work with
# As with the range() function, Python stops one item before the second index you specify
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# This code prints a slice of the list, that includes the first 3 players
# You can generate any subset of a list.
print(players[1:4])
# If you omit the first index in a slice,  Python automatically starts you slice at the beginning of the list
print(players[:4])
# If you want a slice that includes the end of a list, you can start with an index and omit the second index
print(players[2:])
# This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list
# Recall that a negative index returns an element a certain distance from the end of a list, therefor you can output any slice from the end of a list
print(players[-3:])

#* Looping Through a Slice
# You can use a slice in for loop if you want to loop through a subset of the elements in a list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
# Slices are very useful in a number of situations
# Add a score to a list
# Call the player's top 3 scores
# Slices can be used to process data in a chunk of a specific size
