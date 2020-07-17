import math


# PART 1
def my_sqrt(a):
    """Function that takes a as a parameter,
    chooses a starting value for x, and returns an
    estimate of the square root of a."""
    x = 2  # Estimate value for x given default of 2
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return y  # After break, return estimate of square root.


# # TEST my function vs. math module
# print('Part 1:')
# print(my_sqrt(20))
# print(math.sqrt(20))

# print(my_sqrt(25))
# print(math.sqrt(25))
# print('')
# print('Part 2:')


# PART 2
def test_sqrt():
    a = 1
    while a <= 25:
        mysqrt = my_sqrt(a)
        mathsqrt = math.sqrt(a)
        diff = abs(mysqrt - mathsqrt)
        print('a =', a, '| my_sqrt(a) = ', mysqrt, '| math.sqrt(a) =', mathsqrt, "| diff =", diff)
        a += 1


test_sqrt()
