import math


# Example.
def area(radius):
    return math.pi * radius**2


# Return values. All functions should end with a return.
def absolute_value(x, y):
    """6.1 Return values.
    write a compare function takes two values, x and y,
    and returns 1 if x > y, 0ifx == y,and-1ifx < y."""

    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


# absolute_value(4, 0)


# Incremental Development. Use scaffolding and print statements to test parts.
def distance(x1, y1, x2, y2):
    """6.2 Incremental development. Write a function to
    calculate a distance using four coordinate points."""
    xs = (x2 - x1)**2
    ys = (y2 - y1)**2
    result = math.sqrt(xs + ys)
    return result


# distance(1, 2, 4, 6)


# Scaffolding.
def hypotenuse(a, b):
    """ Returns the remaining side of a hypotenuse triangle.
    Requires two arguments for side a and side b."""
    # sides_a_b = a**2 + b**2
    # print("a squared + b squared is ", sides_a_b)
    # print(math.sqrt(sides_a_b))
    return math.sqrt(a**2 + b**2)


# Test if function works:
# hypotenuse(3, 4)


# Composition.
def circle_area(xc, yc, xp, yp):
    """Composition. Calls previous function to get distance between
    center and perimeter of circle. Calculates area of circle."""
    return area(distance(xc, yc, xp, yp))


# Test if function works:
# circle_area(1, 2, 4, 6)


# Boolean Reduction.
def is_divisible(a, b):
    """Checks if value a is divisible by value b. Omit if else."""
    return a % b == 0


# is_divisible(9, 3)
# is_divisible(9, 2)

# Boolean Reduction 2.
def is_between(x, y, z):
    if x < y and y < z:
        print("Yes!")
    else:
        print("No.")
    return x < y < z


def check_me(a, b, c):
    """This demonstrates that each of three values are compared
    between eachother, the second two don't compare against the first."""
    return a > b != c


# IsInstance Function.
def check_value(n):
    """IsInstance function returns boolean if type."""

    if not isinstance(n, int) or n < 0:
        print('This is not a positive integer.')
    else:
        return n, 'is valid.'


# check_value(9.0)
