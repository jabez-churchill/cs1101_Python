# There is something wrong with the arguments the function is getting;
# a precondition is violated.
# Precondition Definition:
# In the context of a precondition to an argument: A condition that must be met before being passed into a parameter. Data type, format, length, number, or other condition... for it to behave as the function is designed.
#
# Explanation:
# Paramaters are set expecting specific data types or objects, as functions are written to use the arguments in specific ways. For example, a function that requires numeric data needed to evaluate math expressions, would choke (RunTime error) if you passed in strings or booleans. Another example would be, a function that changes the character value in a string, revieves a one digit integer, causing a TypeError.

# Example:
def find_first_vowel(term, position):
    """Recursive function to transverse characters of a string,
    prints and returns the first vowel."""
    # Term variable holds a word.
    # Position variable is the index of a word to check.
    if term[position] in ['a', 'e', 'i', 'o', 'u', 'y']:  # Check if a vowel:
        print(term[position])                             # Print first vowel.
    else:                                                 # If not a vowel:
        position += 1                                     # Next index position.
        find_first_vowel(term, position)                  # Recurse with new #


# # Working Call:
# find_first_vowel('Truffle', 0)
# # u
#
# # Precondition Problems:
# find_first_vowel(9, 0)
# # TypeError: 'int' object is not subscriptable
#
# find_first_vowel(True, 0)
# # TypeError: 'bool' object is not subscriptable
#
# find_first_vowel('True', 'zero')
# # TypeError: string indices must be integers



# There is something wrong with the function; a postcondition is violated.
# Postcondition Definition:
# This denotes a problem that happens within a running function. In this case, it's when a function produces an error or undesirable results, even with a valid or appropriate argument has been passed into it.
#
# Explanation:
# When the function fails to do what is expected, even with valid arguments, the function needs to be debugged. It's a great practice to write clear code, in small segments, so that testing each component can be easily identified and tested.


# # Postcondition Problem:
# find_first_vowel('Mr.', 0)
# # IndexError: string index out of range

# I would want this function to accept abbreviations, or at least return something more elegant than a RunTime Error. I would consider this as an example of a postcondition problem. To solve it, I could include another conditional statement as a Guardian, or use a Logical Operator to check if there is a character to traverse to before executing a statement.


def find_first_vowel_v2(term, position):
    if term[position] in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(term[position])
    elif position == len(term)-1:  # Guardian Statement, no letters left.
        print('There are vowels in this word.')
    else:
        position += 1
        find_first_vowel_v2(term, position)


# find_first_vowel_v2('Mr.', 0)
# There are vowels in this word.
#
# find_first_vowel_v2('T', 0)
# There are vowels in this word.


# There is something wrong with the return value or the way it is being used.
# Explanation:
# When a return value is None, the wrong data type, or the wrong format, it can create precondition problems when being called by other functions that expect returns. Below is an example of this. In another function that calls my find_first_vowel_v2 function... after I ask the user to input data, it records both as a string and passess them as arguments. Because my find_first_vowel_v2 requires one string and one integer, we get a RunTime Error. (This can be fixed with a int(input( )) integer constructor around the input function.)

def get_user_input():
    user_word = input('Enter a word to check:  ')
    user_number = input('Enter a position to start from:  ')
    find_first_vowel_v2(user_word, user_number)


# get_user_input()
# Enter a word to check:  Try
# Enter a position to start from:  0
# TypeError: string indices must be integers

# Other Observation: I noticed that Recursive functions that run through conditionals have problems delivering a return, in my own experience. If I call a recursive function, it will not recurse until the top "return" statements are met, it will instantly return None at the end of the first pass! Demonstrated below, if I write my get_user_input() function to PRINT the return value of my find_first_vowel_v3 function.


def find_first_vowel_v3(term, position):
    if term[position] in ['a', 'e', 'i', 'o', 'u', 'y']:
        return term[position]
    elif position == len(term)-1:  # Guardian Statement
        return str('There are vowels in this word.')
    else:
        position += 1
        find_first_vowel_v2(term, position)


def get_user_input_v2():
    user_word = input('Enter a word:  ')
    user_number = int(input('Enter a position:  '))
    print(find_first_vowel_v3(user_word, user_number))


get_user_input_v2()
# Enter a word:  Meaning
# Enter a position:  0
# e
# None
