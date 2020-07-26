# Create a string that is a long series of words separated by spaces.
my_collection = "Jazz Blues Rock Pop Rap RnB Funk Soul J-Pop Electronic Reggae"

# Turn the string into a list of words using split.
my_collection = my_collection.split()


# Delete three words from the list, but delete each one using a different kind of Python operation.
my_collection.pop(7)  # Pop method
del my_collection[1]  # Del method
my_collection.remove('J-Pop')  # Remove method


# Sort the list.
my_collection.sort()


# Add new words to the list (three or more) using three different kinds of Python operation.
my_collection.append('Classical')  # Append method
