
#* Copying a List
# Often you'll want to start with an existing list and maake an entirely new list based on the first one
# Let's explore how copying a list works and examine one situation in which copying a list is useful
# To copy a list, you can make a slice that includes the entire original list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# We make a list of foods then we make list called friends food by asking for a slice of my_foods without specifying any indices and store the copy in frien_foods
# They print the same list
# To prove the lists are different, we will add a new food to each list and show they are kept seperate
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# We add cannoli to my_foods and ice cream to friend_foods
# The lists show different results
# If we had simply set friend_foods equal to my_foods, we would not produce two seperate lists
# Here is what happend when you try to copy a list without using a slice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# Instead of a storing a copy of my_foods in friend_foods, we set friend_foods equal to my_foods.
# This syntax tells Python to connect the new variable friend_foods to the list that is already contained in my_foods, so now both variables point to the same list
# As a result adding cannoli and ice cream will make them appear in both lists