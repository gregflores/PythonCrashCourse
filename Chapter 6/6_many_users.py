
#* A Dictionary in a Dictionary
#  You can nest a dict inside another dict, but your code can get
#  complicated quickly. We'll use several users for a website, with
#  unique usernames as keys.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
# We define a dict with two keys one for each user, then each key is
# associated to a value that is a dict that has first, last, and
# location. Then we loop through the users dict, each username goes in
# the username var, and the dict goes in user_info. We then print out
# the values of each key in user_info