# Exercise 6.4. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.

def is_divisible(x, y):
    return x % y == 0     # Simplified version of original:
                          # if x % y == 0
                          # return True


def is_power(a, b):
    if a == b or b == 1:  # Base case of the two arguments being equal
        return True       # or b equals 1. Recursive functions must
                          # include a base case to resolve. A number
                          # to the power of 0 or 1.
    elif is_divisible(a, b) and is_power(a/b, b):
        # is divisible by b     a/b is a power of b
        return True       # Variable a is a power of variable b.
    else:
        return False      # Not divisible by / to the power of b


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
