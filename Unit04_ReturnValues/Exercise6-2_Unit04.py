import math

# Incremental Development: writing small amount of code at a time.


# STEP 01
# Find the distance between two points, from four coordinates
def distance_v1(x1, y1, x2, y2):
    return 0.0
    # Syntax and input correct format.


# STEP 02
def distance_v2(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)  # Test dx
    print('dy is', dy)  # Test dy
    return 0.0
    # Evaluate parts of equation in parentheses.


# Test if function works:
distance_v2(1, 2, 4, 6)
# dx is 3 √
# dy is 4 √


# STEP 03
def distance_v3(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # print('dx is', dx)
    # print('dy is', dy)
    dsquared = dx**2 + dy**2  # Exponent then addition
    print('dsquared is', dsquared)
    return 0.0


# Test if function works:
distance_v3(1, 2, 4, 6)
# dsquared is 25 √


# STEP 04
def distance_v4(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # print('dx is', dx)
    # print('dy is', dy)
    dsquared = dx**2 + dy**2
    # print('dsquared is', dsquared)
    result = math.sqrt(dsquared)
    return result


# Test if function works:
distance_v4(1, 2, 4, 6)
# 5.0 √
