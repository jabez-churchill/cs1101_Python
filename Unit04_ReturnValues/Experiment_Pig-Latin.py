# Pig Latin Translator
vowel = set(['a', 'e', 'i', 'o', 'u'])
userSentence = []
userOutput = []


def to_piglatin(term, position=0):
    """Translates a word (as argument) to Pig Latin, using string slices
    and recursion."""
    if term[position] in vowel and position == 0:
        # print(term + 'yay')
        return term + 'yay'
    elif term[position] in vowel or position == len(term)-1:
        # print(term[position:] + term[:position] + 'ay')
        return term[position:] + term[:position] + 'ay'
    else:
        position += 1
        to_piglatin(term, position)


# Rules for Pig-Latin
# If vowel, add 'yay' to the end.
# If consenant (followed by vowel), add 'ay'
# If consenant group (followed by vowel), add 'ay'

def input_to():
    q = input('Translate to Pig Latin:  ')
    to_piglatin(str.lower(q))


input_to()


# Iterate through sentence and translate words.
def run_sentence(word=0):
    global userSentence
    global userOutput
    inp = input("Type a sentence to translate:  ")
    userSentence = inp.split()
    if word == len(userSentence):
        print(userOutput)
    else:
        userOutput = userOutput + to_piglatin(userSentence[word])
