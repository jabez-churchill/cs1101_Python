def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


any_lowercase1('nice')  # True
any_lowercase1('Naughty')  # False
any_lowercase1('poWer')  # True

# This first example seems to only check the first letter of a string.

# NOTE: The local variable in a For loop is declared in its first
# line. For example... for _x_ in range_of_counting. i = Indices
