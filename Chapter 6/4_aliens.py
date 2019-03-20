
#* Nesting
#  Sometimes you'll want to store a set of dictionaries in a list or a
#  list of items as a value in a dictionary. This  is called nesting.
#  You can nest a set of dictionaries inside a list, a list of items
#  inside a dict, or even a dict inside a dict

#* A list of Dictionaries
#  The alien_0 dictionary contains a variety of information about one
#  alien, but it has no room to store info about a second alien, much
#  less a fleet of aliens.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# We create 3 dicts representing different alians. We create a list of
# the aliens and print them all out. A more realistic example would
# involve more than 3 aliens with code that automatically generates each
# alien.

# Make an empty list for storing aliens
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')
# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
# This example begins with an empty list to hold all of the aliens. We
# then return a set a numbers with range() to loop through, and for
# every loop we create a new alien and append it to the list. These
# aliens all have the same characteristics, but Python considers each
# one a seperate object, which allows us to modify each alien
# individually. Imagine some aliens change color and move faster as the
# game progresses. When it's time to change colors, we can use a for
# loop and an if statement to change the color of aliens

# Make an empty list for storing aliens
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print('...')        
# We modify the first 3 aliens using a slice. We are only modifying the
# green aliens. You could use an elif block to change yellow aliens to
# red aliens. 