# Pig Latin Translator
vowel = set(['a', 'e', 'i', 'o', 'u'])


def to_piglatin(term, position=0):
    build = ''
    beginning = ''
    if term[position] in vowel and position == 0:
        return term + 'ay'
    # finished... found a vowel
    elif term[position] in vowel:
        return build + beginning + 'ay'
    else:
        print("Not a vowel")
        build = build + term[position]
        beginning = beginning + term[position]
        position += 1
        to_piglatin(term, position)


to_piglatin('Win')
to_piglatin('off')

# Rules for Pig-Latin
# If vowel, add 'yay' to the end.
# If consenant (followed by vowel), add 'ay'
# If consenant group (followed by vowel), add 'ay'

# ending is word's
