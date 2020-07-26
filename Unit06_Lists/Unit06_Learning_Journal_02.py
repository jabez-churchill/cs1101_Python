# PART TWO
# Provide your own examples of the following using Python lists.
# Create your own examples.

def print_separator():
    print('')
    print('')


# Nested lists
print("1. Nested lists: Lists can contain other lists as elements.")

full_list = [['Bono', 'Cher', 'Lady Gaga'], [1960, 1946, 1986], ['Rock', 'Pop', 'Dance']]

print(full_list)
print_separator()


# The “*” operator
print("2. The * operator: Multiply iterable objects.")

thrice = ['item'] * 3
print("Print ['item'] * 3")
print(thrice)
print_separator()
# ['item', 'item', 'item']


# List slices
print("3. List slices: select a range of elements from a list.")

fav_subject = ['Math', 'Science', 'English', 'Thai', 'Computer Science', 'Art']
print(fav_subject)

last_two = fav_subject[-2:]  # Slice from second to last, to the last value of the list.
print("The last two elements are", last_two)
print_separator()
# ['Computer Science', 'Art']



# The “+=” operator
print('4. The "+=" operator: increment or add to an element.')

fav_hobbies = ['Gaming', 'Art', 'Football', 'Music', 'Reading']
print(fav_hobbies)
print('___________')

print('Add "YouTube" to fav_hobbies with +=')
print('Print each list element with an accumulator using +=.')
fav_hobbies += ['YouTube']  # Add an iterable item (from list, tuple, etc)
# ['Gaming', 'Art', 'Football', 'Music', 'Reading', 'YouTube']

# The += operator from the textbook example, as an "accumulator"
count = 1  # Start counter at one.
for i in fav_hobbies:
    print(count, i)
    count += 1  # Add one to accumulator.
print_separator()

# OUTPUT:
# 1 Gaming
# 2 Art
# 3 Football
# 4 Music
# 5 Reading
# 6 YouTube



# A list filter
print("5. List filter: methods that evaluate depeneding on a boolean condition")

key_years = [1971, 1977, 1978, 1982, 1988, 1994, 1999, 2000, 2001, 2005]

print("Key Years in the 70's")
for year in key_years:
    if str(year).__contains__('197'):
        print(year)

print_separator()


# The filter function
print("Filter function: a built-in function accepting a custom function against an iterable object.")


def is_even(a_year):
    if a_year % 2 == 0:
        return True
    else:
        return False



# The filter function checks iterable objects against a custom boolean conditional.
filtered_years = filter(is_even, key_years)


def filter_years():
    for year in filtered_years:
        print(year)

print('Years that are even numbers:')
filter_years()
print_separator()
# 1978
# 1982
# 1988
# 1994
# 2000


# A list operation that is legal but does the "wrong" thing, not what the programmer expects
print("6. A common mistake: changing iterable items to NoneType")
# List methods generally return NONE, so writing assignment statements in the
# same was as you would for strings, will basically clear your list!
grade_levels = ['1st', '2nd', '3rd', '4th', '5th', '6th']
print(grade_levels)

# Assigning a NoneType return to a variable.
grade_levels = grade_levels.sort()
print('The variable now is... ', grade_levels)
