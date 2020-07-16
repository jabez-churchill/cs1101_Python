# Pig Latin Translator
vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])


def to_piglatin(term, position=0):
    """Prints a word (as argument) to Pig Latin, using string slices
    and returns."""

    while term[position] not in vowel and position < len(term):
        position += 1

    if term[position] in vowel and position == 0:
        return str(term + 'yay')
    elif term[position] in vowel or position == len(term)-1:
        return str(term[position:] + term[:position] + 'ay')
    else:
        return str('')


# Rules for Pig-Latin
# If vowel, add 'yay' to the end.
# If consenant or group, move behind first vowel and add 'ay'


def get_sentence():
    """User inputted string, converts it to a list. """

    sen = str.lower(input('Write a sentence to translate:  '))
    userSentence = sen.split()
    translate_sen(userSentence)


def translate_sen(senlist, pos=0):
    """Iterates through each word of list, calls to_piglatin prints each."""
    output = ''
    while pos < len(senlist):
        output = output + to_piglatin(senlist[pos]) + ' '
        pos += 1
    print(output)


get_sentence()
