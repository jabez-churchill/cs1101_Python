# check whether a string contains ANY lowercase letters

def any_lowercase1(s):
    for c in s:
        if c.islower():
            print(c, 'is lower case')  # Added to check indices.
            return True
        else:
            print(c, ' is not lowercase')
            return False  # This loop ends at the FIRST upper case letter.
            # Won't check a whole word.


# OUTPUT
any_lowercase1('try')
# t is lower case
# True
any_lowercase1('Try')
# T  is not lowercase
# False
any_lowercase1('TRY')
# T  is not lowercase
# False

# This first example ends with a return if the first letter is upper case,
# so it fails to loop and check if ANY lowercase letters in the whole string.
# You can see that only one iteration was printed for each


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():  # Checking an immutable string 'c', not variable c.
            return 'True'  # Returns a string object 'True', not boolean.
        else:
            return 'False'  # Returns a string object 'False', not boolean.


# OUTPUT
any_lowercase2('try')
# True
any_lowercase2('Try')
# True
any_lowercase2('TRY')
# True

# This function uses string objects inappropreatly. The first if statement is
# evaluating a string object 'c' and will always evaulate to True.


def any_lowercase3(s):
    for c in s:
        print(c, c.islower())  # Add print statement to check each index
        flag = c.islower()
    return flag  # Returns the last assigned boolean value of c.islower.


# OUTPUT
any_lowercase3('try')
# t True
# r True
# y True
# True
any_lowercase3('Try')
# T False
# r True
# y True
# True
any_lowercase3('TRY')
# T False
# R False
# Y False
# False
any_lowercase3('TrY')
# T False
# r True
# Y False
# False

# This function loops / iterates through all characters in a string, but never
# breaks the loop if a lower case letter is found. It simply returns the
# boolean value of the last letter in the string.


def any_lowercase4(s):
    flag = False
    for c in s:
        print(c, flag)  # Added print statement to check state before.
        flag = flag or c.islower()  # previous OR current index are lowercase.
        print('to ', flag)  # Added print statement to check updated state.
    return flag


# OUTPUT
any_lowercase4('try')
any_lowercase4('Try')
any_lowercase4('TRY')
any_lowercase4('TrY')
# T False
# to  False
# r False
# to  True
# Y True
# to  True
# True

# This function seems to work. It updates a boolean value to true if the
# current OR any previous values were true. Even cycling through all the
# characters of a string without breaking, it retains any True value found.


def any_lowercase5(s):
    for c in s:
        if not c.islower():  # If ANY character is not lower case...
            print(c, 'is not lower.')  # Print where loop ends.
            return False  # ... break the loop and return False.
    return True  # No characters in the loop were NOT lower case, return True.


# OUTPUT
any_lowercase5('try')
# True
any_lowercase5('Try')
# T is not lower.
# False
any_lowercase5('TRY')
# T is not lower.
# False
any_lowercase5('trY')
# Y is not lower.
# False

# This is almost a good function, but it's backwards. The idea here is to
# end the loop at some point instead of iterating through characters needlessly
# but it breaks when ANY capial letter is found. The point of this function is
# to find if any lower case letters are in a string. A working example of
# breaking a loop, would be breaking when any lower case letter is found, else
# return True. Example:


def any_lowercase6(s):
    for c in s:
        if c.islower():
            return True
    return False


# OUTPUT
any_lowercase6('try')
# True
any_lowercase6('Try')
# True
any_lowercase6('TRY')
# False
any_lowercase6('TrY')
# True
any_lowercase6('trY')
# True
