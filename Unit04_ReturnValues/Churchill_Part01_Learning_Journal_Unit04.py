import math
# Part One - - - - - - - - - - - - - - - - - - -


# STEP 01
def hypotenuse_v1(a, b):
    return 0.0
    # Syntax and parameters valid.


# STEP 02
def hypotenuse_v2(a, b):
    sides_added = a**2 + b**2
    print(a, 'squared plus', b, 'squared is', sides_added)  # Check addition.
    return 0.0


# Test if function works:
# hypotenuse_v2(3, 4)
# a squared plus b squared is 25 √


# STEP 03
def hypotenuse_v3(a, b):
    sides_added = a**2 + b**2  # Confirmed working.
    # print(a, 'squared plus', b, 'squared is', sides_added)
    result = math.sqrt(sides_added)  # Evaluate result.
    return result


# Test if function works:
# hypotenuse_v3(3, 4)
# 5.0 √


# STEP 04
def hypotenuse(a, b):  # Remove scaffolding, as long as code is understandable.
    return (math.sqrt(a**2 + b**2))


# Final Call
hypotenuse(3, 4)
hypotenuse(5, 12)
hypotenuse(80, 18)

# >>> hypotenuse(3, 4)
# 5.0
# >>> hypotenuse(5, 12)
# 13.0
# >>> hypotenuse(80, 18)
# 82.0
