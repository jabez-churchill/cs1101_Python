# Pig Latin Translator
vowel = set(['a', 'e', 'i', 'o', 'u'])


def to_piglatin(term, position=0):
    """Translates a word (as argument) to Pig Latin, using string slices
    and recursion."""
    while term[position] not in vowel:
        position += 1
    if term[position] in vowel and position == 0:
        # print(term + 'yay')
        return str(term + 'yay')
    elif term[position] in vowel or position == len(term)-1:
        # print(term[position:] + term[:position] + 'ay')
        return str(term[position:] + term[:position] + 'ay')
    else:
        # if not a vowel and not last letter
        return str(term[position:] + term[position] + 'ay')
        # position += 1
        # to_piglatin(term, position)


# Rules for Pig-Latin
# If vowel, add 'yay' to the end.
# If consenant (followed by vowel), add 'ay'
# If consenant group (followed by vowel), add 'ay'

def input_to():
    q = input('Translate to Pig Latin:  ')
    to_piglatin(str.lower(q))


# input_to()


# Get Sentence
def get_sentence():
    sen = str.lower(input('Write a sentence to translate:  '))
    userSentence = sen.split()
    print(userSentence)
    translate_sen(userSentence)


def translate_sen(senlist, pos=0):
    output = ''
    while pos < len(senlist):
        output = output + to_piglatin(senlist[pos]) + ' '
        pos += 1
    print(output)
    # print(output)


get_sentence()

# Iterate through sentence and translate words.
# def run_sentence(word=0):
    # global userSentence
    # global userOutput
    # inp = input("Type a sentence to translate:  ")
    # userSentence = inp.split()
    # if word == len(userSentence):
    #     print(userOutput)
    # else:
    #     userOutput = userOutput + to_piglatin(userSentence[word])
