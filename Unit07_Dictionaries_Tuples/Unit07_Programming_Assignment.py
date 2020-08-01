# Start with the following Python code.
alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


# From Section 11.2
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# PART ONE:
# Write a function called has_duplicates that takes a string parameter and
# returns True if the string has any repeated characters. Otherwise, it
# should return False.
def has_duplicates(a_string):
    letters = histogram(a_string)  # Store the histogram function result.
    for letter in letters.values():  # Iterates through each value.
        if letter > 1:  # If more than one instance is found...
            return True
    return False  # The loop finished the whole word without finding duplicate.


# Write a loop over the strings in the provided test_dups list. Print each
# string in the list and whether or not it has any duplicates.
print("")
print("Part 1: Loop over test_dups and print if each has duplicates or not.")
print("_"*70)

for i in test_dups:
    if has_duplicates(i):
        print(i, "has duplicates.")
    else:
        print(i, "has no duplicates")


# PART TWO
# Write a function called missing_letters that takes a string parameter and
# returns a new string with all the letters of the alphabet that are not in
# the argument string.
def missing_letters(a_string):
    global alphabet  # Link the global variable, non-local.
    are_missing = []  # Initialize a list object to record missing letters.
    letter_collection = histogram(a_string.lower())  # Ignore case.
    for letter in alphabet:  # Iterate through global alphabet
        if letter not in letter_collection.keys():  # If not in string...
            are_missing.append(letter)  # Add letter to list.
    result = ''.join(are_missing)  # Join list items to string.
    return result


# Loop over the strings in list test_miss and call missing_letters with each
# string. Print a line for each string listing the missing letters.
print("")
print("Part 2: Print a line for each string listing the missing letters.")
print("_"*70)

for i in test_miss:
    if missing_letters(i):  # If not returning NoneType
        print(i, "is missing letters", missing_letters(i))
    else:  # Returned None, has all letters.
        print(i, "uses all the letters.")
