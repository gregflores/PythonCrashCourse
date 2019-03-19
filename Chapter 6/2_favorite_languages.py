
#* A Dictionary of Similar Objects
# The previous example involved storing different kinds of information about one object
# You can also use a dict to store one kind of information about many objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# As you can see we've broken a larger dictionary into several lines. Each key is the name of a person who responded to the poll, and each value is there language of choice
# To use this dict, given the name of a person who took the poll, you can easily look up their favorite language
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
# Python loops through each pair in the dict

#* Looping Through All the Keys in a Dictionary
# The keys() method is useful when you don't need to work with all of the values in a dictionary
for name in favorite_languages.keys():
    print(name.title())
# Looping through keys is the default behavior. The above code behaves the same as
for name in favorite_languages:
    print(name.title())
#You can access the value associated with any key you care about inside the loop by using the current key
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
# We make a list of friends that we want to print a message to.
# Inside the loop, we print each person's name
# Check fi the name is in the friends list
# You can also use the keys() method to check if a person was polled
if 'erin' not in favorite_languages.keys():
    print('Erin, please take out poll!')

#* Looping Through a Dictionary's Keys in Order
# A dict always maintains a clear connection between each key and value, but you never get the items from a dict in any predictable order
# That's not a problem because you usually just want to obtain the correct value associated with each key
# You can use the sorted() functiuon to get a copy of the keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
# This for statement is like other for statements except we've wrappped the sorted() function around the dict.keys() method.
# This tells python to list all keys in the dict and sort the list before looping through it

#* Looping Through All Values in a Dictionary
# If you are primarily interested in the values that a dict contains, you can use the values() method to return a list of values without any keys
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# This approach pulls all the value from the dict without checking for repeats
# To see each without repetition we can use a set
# Similar to a list except each item in a set must be unique
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#When you wrap set() around a list that contains duplicates, Python identifies the unique items and builds a set from those items