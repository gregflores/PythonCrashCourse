
#! PAGE 53

#* Working with Lists

#* Looping Through an Entire List
# You'll often want to run through all entries in a list, performing the same task with each item.
# When you want to do the same action with every item in a list, you can use Python's for loop
# Let's say we want to print out each name in a list
# This can be done by calling each item individually, but could be very long and repetitive for long lists
# You would also have to change the code for different lengths of lists
# A for loop avoids both issues by letting Python manage these issues internally
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
# We begin by defining a list
# Then we define a for loop
# This line tells Python to pull a name from the list magicians, and store it in the variable magician
# We then print out what was just stored in magician
# Python repeats the for and print for each name in the list
# "For every magician in the list of magicians, print the magicians name."

#* Doing More Work Within a for Loop
# You can do just about anything with each item in a for loop.
# Let's build on the previous example by printint a message to each magician
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# You can also write as many lines of code as you like in the for loop
# Every indented line following the line for magician in magicians is considered inside the loop
# Each indented line is executed once for each value in the list.
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " +magician.title() + ".\n")

#* Doing Something After a for Loop
# Any lines of code after a for loop that are not indented are executed once without repetition.
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " +magician.title() + ".\n")
print("Thank you, everyone. That was a great show!")
