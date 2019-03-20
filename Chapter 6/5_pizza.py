
#* A list in a dictionary
#  Rather than putting a dict in a list, it's sometimes useful to put a
#  list inside a dictionary. For example, consider how you might
#  describe a pizza that someone is ordering. If you use only a list,
#  all you could really store are the toppings. With a dict, a list of
#  toppings can be just one aspect of the pizza you're describing. In
#  the following example two kinds of info are stored for each pizza, a
#  type of crust and a list of toppings

# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# We begein with a dict that holds information about a pizza that has
# been ordered. One key in the dictionary is 'crust', and the other is a
# list of toppings. We then summarize the order using a for loop for the
# toppings.
