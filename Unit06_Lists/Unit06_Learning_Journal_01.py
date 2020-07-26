# PART ONE
# Create a string that is a long series of words separated by spaces.
my_string = "Jazz Blues Rock Pop Rap RnB Funk Soul J-Pop Electronic Reggae"

# Turn the string into a list of words using split.
my_collection = my_string.split()


# Delete three words from the list, but delete each one using a different kind of Python operation.
my_collection.pop(7)  # Pop method
del my_collection[1]  # Del method
my_collection.remove('J-Pop')  # Remove method, search and remove (GeeksForGeeks, 2018)


# Sort the list.
my_collection.sort()  # Reorganizes values in alphabetical order by default.


# Add new words to the list (three or more) using three different kinds of Python operation.
more_music = ['Techno', 'Trance']

my_collection.extend(more_music)  # Exend method: Adds iterable objects.
my_collection.insert(3, 'Metal')  # Insert method: Inserts to index (1st argument)
my_collection.append('World')  # Append method: Adds to end of list.

# Variations of append.
my_collection = my_collection + ['Latin']
my_collection += ['Dance']

# Turn the list of words back into a single string using join.
my_string = ' '  # This will be the separator between each iterable value.
my_string = my_string.join(my_collection)  # Join method combines iterable values. (Programiz, n.d)


# Print the string.
print(my_string)
# 'Electronic Funk Jazz Metal Pop Rap Reggae RnB Rock Techno Trance World Latin Dance'


# References:

# Programiz. (n.d.). Python List remove(). Python List Methods.
# Retrieved from https://www.programiz.com/python-programming/methods/list/remove

# GeeksForGeeks: join() function in Python. (2018, January 2). GeeksforGeeks.
# Retrieved from https://www.geeksforgeeks.org/join-function-python/
