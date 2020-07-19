def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


any_lowercase5('True')
any_lowercase5('true')
any_lowercase5('truE')


def any_lowercase5(s):
    for c in s:
        if not c.islower():  # If ANY character is not lower case...
            print(c, 'is not lower.')  # Print where loop ends.
            return False  # ... break the loop and return False.
    return True  # No characters in the loop were NOT lower case, return True.


def any_lowercase(s):
    for c in s:
        if c.islower():
            return True
    return False


any_lowercase('True')
any_lowercase('true')
any_lowercase('truE')
any_lowercase('TRUE')
