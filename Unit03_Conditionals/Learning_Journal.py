# EXAMPLE 1
# Copy the countdown function from Section 5.8 of your textbook.
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


# Write a new recursive function countup that expects a negative
# argument and counts “up” from that number.
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


# Write a Python program that gets a number using keyboard input.
def start_count():

    number = int(input('Enter a number: '))

    if number > 0:
        countdown(number)
    elif number < 0:
        countup(number)
    else:
        print('Enter a positive or negative number. Not zero.')
        start_count()


start_count()


# EXAMPLE 2
# Write your own unique Python program that has a runtime error.
def exponent_error():
    """Prints a number to the power of five."""
    number1 = input('Enter a number: ')

    print(number1**5)

# exponent_error()


# Demonstration of how to fix the error.
def no_error():
    """Prints a number to the power of five."""
    number1 = int(input('Enter a number: '))  # Integer constructor!

    print(number1**5)


# This function will take user input and raise it to the power of five.
no_error()
