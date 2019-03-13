
#* Whitespace
# Whitespace refers to any nonprinting character
# Space, tabs, end-of-line
# Whitespace can be used to organize your output
# \t for tab
print("Python")
print("\tPython")

# \n for newline
print("Languages:\nPython\nC\nJavaScript")

# You can combine tabs and newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#* Whitespace
# Whitespace can be confusing in your programs
# To programmers 'python' and 'python ' look the same, but to a program they are different strings
# Python detects the extra space in 'python ' and considers it important
# Python can look for extra whitespace on the right and left sides of a string
# To ensure that no whitespace exists at the right end of a string use the rstrip() method

favorite_language = 'python '
print("'" + favorite_language + "'")
print("'" + favorite_language.rstrip() + "'")
print("'" + favorite_language + "'")

# The value stored at favorite_language contains extra whitespace
# When printing the value you can see the extra whitespace
# When rstrip() method acts on the var the extra space is removed, but only temporarily
# When you ask for the value of favorite_language again, you can see that the string looks the same as when it was entered with the extra whitespace
# To remove the whitespace from the string permanently, you have to store the stripped value back into the variable
favorite_language = 'python '
print("'" + favorite_language + "'")
favorite_language = favorite_language.rstrip()
print("'" + favorite_language + "'")

#You can strip whitespace from the left side of a string using the lstrip() method or strip whitespace from both sides at once using strip()

favorite_language = ' python '
print("'" + favorite_language + "'")
print("'" + favorite_language.rstrip() + "'")
print("'" + favorite_language.lstrip() + "'")
print("'" + favorite_language.strip() + "'")
print("'" + favorite_language + "'")