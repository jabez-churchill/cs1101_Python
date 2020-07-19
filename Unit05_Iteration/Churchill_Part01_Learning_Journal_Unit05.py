# Exercise: Section 8.3
prefixes = 'JKLMNOPQ'
suffix = 'ack'


def martian():
    for letters in prefixes:
        if letters == 'O' or letters == 'Q':  # Conditional if "O" or "Q"
            letters = letters + 'u'  # Concatenate "u"
        print(letters + suffix)


# OUTPUT:
martian()
# Jack
# Kack
# Lack
# Mack
# Nack
# Ouack
# Pack
# Quack
