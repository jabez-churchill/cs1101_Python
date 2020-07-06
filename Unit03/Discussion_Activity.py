# Describe the difference between a chained conditional and a nested conditional.

# Chained conditional:
# A conditional statement with a series of alternative branches.

def chained_conditional(word1, word2):
    """Function to put two strings in alphabetical order"""

    if type(word1)!= str or type(word2) != str:
        print('Arguments must be in string format')

    elif word1[0] < word2[0]:       # if the first letter is less / smaller position
        print(word1, word2)         # print this word first, the order word second

    elif word1[0] > word2[0]:       # if the first letter is more / larger position
        print(word2, word1)         # print the other word first, this word second

    elif word1[1] < word2[1]:       # logically, if the first letter isn't more or less,
        print(word1, word2)         # they're equal, and we compare the second letter
                                    # print the word with a higher position[1] first.
    else:
        print(word2, word1)         # or else the last possible outcome.


def get_words():
    word1 = input('First word to alphebetize: ')
    word2 = input('Second word to alphabetize: ')
    chained_conditional(word1, word2)


#get_words()


# Nested Conditional
# A conditional statement that appears in one of the branches of another
# conditional statement.

def nested_conditional(word_a, word_b):
    """Put arguments in alphabetical order, up to two letters."""

    i = 0

    if word_a[i] == word_b[i]:
        i += 1

        if word_a[i] < word_b[i]:   # Here is a nested conditional. We can keep
            print(word_a, word_b)   # nesting more and more 'if statements' to
                                    # compare further letter positions.
        else:
            print(word_b, word_a)

    elif word_a[i] < word_b:
        print(word_a, word_b)

    else:
        print(word_b, word_a)


def ask_for_words():
    word_a = input('Enter a word to alphatize: ')
    word_b = input('Enter another word to alpabetize: ')
    nested_conditional(word_a, word_b)


# ask_for_words()



# Avoiding Nested Conditionals
# Logical operators (such as and, or, not) can be used to combine several conditions into one statement.
# For my example above, I found that recursion was a more functional solution to avoid nested conditionals, as the function calls itself passing an updated position to check if the letters being compared are the same, forever.



def letter_checker(word_a, word_b, position = 0):
    """Puts two words in alphabetical order. Unlimited position checks."""

    if word_a[position] < word_b[position]:
        print(word_a, word_b)

    elif word_a[position] > word_b[position]:
        print(word_b, word_a)

    else:                       # Letters must be equal. Update the postion to check.
        position += 1
        letter_checker(word_a, word_b, position) # Call this function again with new position.



def get_input():
    word_a = input('Enter a word to alphabetize: ')
    word_b = input('Enter another word to alpabetize: ')

    if word_a == word_b:        # If the two words are the same, avoid an error.
        print('These words are the same, please enter different words.')
        get_input()             # Start over!
    elif len(word_a) < len(word_b):
        word_a = word_a + ' '*(len(word_b) - len(word_a))
    elif len(word_a) > len(word_b):
        word_b = word_b + ' '*(len(word_a) - len(word_b))
    return letter_checker(word_a, word_b)


get_input()
