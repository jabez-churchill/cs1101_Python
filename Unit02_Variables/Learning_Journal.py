# LEARNING JOURNAL: UNIT 2

# Part 1 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
print('Part 1: Volume of a Sphere')
# Write a function called print_volume (r) that takes an argument for
# the radius of the sphere, and prints the volume of the sphere.

# 1.1 The code for your print_volume function.
import math


def print_volume(r):
    sphere = 4/3 * math.pi * r**3
    print(sphere)


# 1.2 The inputs and outputs to three calls of your print_volume.
print('Volume of sphere:')

print_volume(3)
# OUTPUT: 113.09733552923254 Confirmed correct.

print_volume(6.9)
# OUTPUT: 1376.0552813841728 Confirmed correct.

print_volume(55.5)
# OUTPUT: 716089.917070277 Confirmed correct.




# Part 2 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
print('Part 2: My function.')
# Write your own function that illustrates a feature that you learned
# in this unit. The function must take at least one argument.


def print_savings(newprice, sav):
    format_newprice = round(newprice, 2)
    format_sav = round(sav, 2)
    print(' ')
    print('Your item on sale is $', format_newprice)
    print('You save $', format_sav)


def sale_calc(price, percent_off=1):
    savings = percent_off / 100 * price
    discounted = price - savings
    print_savings(discounted, savings)


def sale_data():
    item_price = input("How many dollars does the item cost? ")
    item_percent_off = input("What's the percent off? ")
    # Ask user to enter the price of an item, and the percent-off of a sale.
    # After assigning user-input data to each variable.
    sale_calc(float(item_price), float(item_percent_off))
    # A "float constructor" is used to convert each inputed
    # string object to a float.

# This statement executes our sale_calc function and passess the two
# user-input data objets into it's parameters, as float objects.


# RUN
sale_data()

#   |
#   V
#
# ORDER OF EXECUTION
#
#   0. Call sale_data function.
#
# -sale_data-
#   1. User inputs string objects, assigned to variables. Saves the
#      original item price and percent-off of a sale.
#   2. Call sale_calc function, passing variables as arguments,
#      which are converted to float objects while assigned.
#
# -sale_calc-
#   3. Savings is calculated at percent / 100 * item price.
#   4. Discounted price of item calculated by subtracting savings from price.
#   5. Call print_savings function, passing new price and savings as args.
#
# -print_savings-
#   6. Format new price with round function, omit all but two decimal places.
#   7. Format savings with round function, omit all but two decimal places.
#   8. Print a sentence that informs user how much the item costs on sale,
#      and how much they've saved.


# Part 3 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
print('Part 3: My argumentative function.')


def my_argument(arg):
    print("You're wrong! I can't find the article I read before, but it validates my intuition.")
    print("I can't believe you think", arg)


def common_argument():
    your_opinion = input("Write one opinion people people don't agree with: ")
    my_argument(your_opinion)


common_argument()
