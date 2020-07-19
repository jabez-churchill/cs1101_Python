# EXAMPLE THREE
# Pig Latin Translator
vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])


def to_piglatin(term, position=0):
    """Accepts one word, translates to Pig Latin and returns,
    using string slices."""

    while term[position] not in vowel and position < len(term):
        position += 1  # Locate the index of the first vowel.

    if term[position] in vowel and position == 0:
        return str(term + 'yay')  # If vowel, add 'yay' to the end.
    elif term[position] in vowel or position == len(term)-1:
        return str(term[position:] + term[:position] + 'ay')
        # If consenant or group, move behind first vowel and add 'ay'
    else:
        return str('')


def get_sentence():
    """User inputted string, converts it to a list
    and passes to translate_sen to evaluate each word. """

    sen = str.lower(input('Write a sentence to translate:  '))
    sen.strip('.')
    userSentence = sen.split()
    translate_sen(userSentence)


def translate_sen(senlist, pos=0):
    """Iterates through each word of list, calls to_piglatin
    and prints each return."""
    output = ''
    while pos < len(senlist):
        output = output + to_piglatin(senlist[pos]) + ' '
        pos += 1
    print(output)


get_sentence()
