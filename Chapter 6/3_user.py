
#* Looping Through a Dictionary
# A single Python dict can contain just a few pairs or millions of pairs
# Python lets you loop through a dict
# There are several ways to loop through them
# Through its key-value pairs, keys, or values

#* Looping through all key-value pairs
# You can access a single piece of info about user_0, but what if you wanted to see eveything stored in this user's dict?
# Loop with a for loop
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# To write a for loop for a dict, you create names for the two vars that will hold the key and value in each pair
# You can choose any names for these vars
# The second half of the for loop includes the name of the dict followed by the method items(), which returns a list of key-value pairs.
# Values don't have to be returned in the order they were stored
# Looping through all key-value pairs works particularly well for dicts which store similar information for many different keys