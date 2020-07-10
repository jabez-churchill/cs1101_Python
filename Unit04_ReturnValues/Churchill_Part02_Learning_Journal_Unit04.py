# Pig Latin Translator
# Based on my Discussion Activity experiment, returning the first vowel in a word, I'm going to attempt to make a pig latin translator. The rules of pig latin are:
# If vowel, add 'yay' to the end.
# Any cosenent before the first vowel, moves to the end of the word plus 'ay'.
# Any consenet group before the first vowel, moves to the end plus 'ay'.

# Create a set of vowels.
vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])


# STEP 01
def english_to_piglatin_v1(term, position=0):
    return 'end'
    # Set up the function with two parameters, term holds the english word as string object, and position is an integer to check the index of the string during recursion. Position has a default value of 0, so an argument isn't needed on the first call.


# STEP 02
def english_to_piglatin_v2(term, position=0):
    if term[position] in vowel:     # Rule: if a vowel
        print(term + 'yay')         # add 'yay' to the end.
    else:                           # The easy part.
        return 'end'


english_to_piglatin_v2('apple')
# appleyay √
english_to_piglatin_v2('Orange')
# end !!
# Discovered that the characters are case sensitive.
# >>> 'a' == 'a'
# True
# >>> 'a' == 'A'
# False
# >>> str.lower('A') == 'a'
# True
# This is a possibile solution, but not sure where it belongs yet.

# How do I separate a word by index position?

# Stuck here. While trying to find the best way of moving part of a string to the back of a word, I discovered string slices! Using two integers separated by a colon, inside square brackets following a string object; you can select a group! This seems perfect because I'm keeping track of an index position.
# >>> 'interesting'[4:8]
# 'rest'

# New order:
# 1. Identify the first vowel with recursion.
# 2. Print the string slice including and following the vowel.
# 3. Concatenate the string slice before the vowel.
# 4. Concatenate the string 'ay'.

# STEP 03
def english_to_piglatin_v3(term, position=0):
    if term[position] not in vowel:
        position += 1   # Move to next index position
        english_to_piglatin_v3(term, position)  # Recurse
    else:
        print(position)  # Test the vowel position is correctly identified


# Test finding a vowel:
english_to_piglatin_v3('find')
1
english_to_piglatin_v3('fly')
2


# STEP 04
def english_to_piglatin_v4(term, position=0):
    if term[position] in vowel and position == 0:
        print(term + 'yay')
    elif term[position] not in vowel:
        position += 1
        english_to_piglatin_v4(term, position)
    else:
        print(term[position:] + term[:position] + 'ay')
            # [position:] is the same as [vowel:last letter]
            # [:postion] is like [first letter:vowel]


english_to_piglatin_v4('Fruit')
# uitFray √
english_to_piglatin_v4('apple')
# appleyay √
english_to_piglatin_v4('a')
# ayay √
english_to_piglatin_v4('Mr.')
# IndexError: string index out of range !!


# STEP 05
def english_to_piglatin_v5(term, position=0):
    # In case there are no vowels, added an OR logical operator to return.
    if term[position] in vowel and position == 0 or position == len(term)-1:
        print(term + 'yay')
    elif term[position] not in vowel:
        position += 1
        english_to_piglatin_v5(term, position)
    else:
        print(term[position:] + term[:position] + 'ay')


english_to_piglatin_v5('Fruit')
# uitFray √
english_to_piglatin_v5('apple')
# appleyay √
english_to_piglatin_v5('a')
# ayay √
english_to_piglatin_v5('Mr.')
# Mr.yay √
