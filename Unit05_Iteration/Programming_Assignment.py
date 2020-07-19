import math


# PART 1
def my_sqrt(a):  # CRITERIA 1: Include 1 parameter.
    """Function that takes a as a parameter,
    chooses a starting value for x, and returns an
    estimate of the square root of a."""
    x = 2  # # CRITERIA 2: Initialize x
    while True:  # CRITERIA 1: Include while loop.
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y  # CRITERIA 2: Return final value of x
    return y  # After break, return estimate of square root.


# PART 2
def test_sqrt():
    a = 1
    while a <= 25:  # CRITERIA 3: Print index of 1 - 25
        mysqrt = my_sqrt(a)  # CRITERIA 4: Print values of my_sqrt
        mathsqrt = math.sqrt(a)  # CRITERIA 5: Print values of math.sqrt
        diff = abs(mysqrt - mathsqrt)  # CRITERIA 6: Print values of diff
        print('a =', a, '| my_sqrt(a) = ', mysqrt, '| math.sqrt(a) =', mathsqrt, "| diff =", diff)
        a += 1


test_sqrt()
