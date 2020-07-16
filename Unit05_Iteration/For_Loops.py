my_list = [1, 2, 3, 4, 5]

# Daddy finger song lyrics generator.
finger_list = ['Daddy', 'Mommy', 'Brother', 'Sister', 'Baby']


def finger_family():
    for i in range(len(finger_list)):
        print(finger_vers(finger_list[i] + ' finger'))
        print('')


def finger_vers(finger_name):
    v1 = ", "
    v2 = "where are you? "
    v3 = "Here I am. "
    v4 = "How do you do? "
    vers = finger_name + v1 + finger_name + v1 + v2 + v3 + v3 + v4
    return vers


# # TEST
# >>> finger_verse('fish finger')
# # 'fish finger, fish fingerwhere are you? Here I am. How do you do? '

# # TEST
# finger_family()

# Basic For Loop
def run_loop(list):
    for number in list:
        print('Hello')


# run_loop(my_list)


# Loop In Range
def run_range():
    """For loop runs between range of 2 and 30, count by 2s."""

    for number in range(2, 30, 2):  # Between 2 and 30, by twos
        print(number, 'is in range.')


# run_range(my_list)


def another_range(word, pos=0):
    """For loop runs each position of string inputted."""
    for number in range(pos, len(word)):
        print(word[pos], "is number", number)
        pos += 1


# another_range('America')
# another_range('America', 4)  # Last three letters

# EXERCISE 8.6 SEARCHING
def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


# EXERCISE 8.7 COUNTING
def count_v1(word, check_letter):
    counter = 0
    for letter in word:
        if letter == check_letter:
            counter += 1
    print(letter)
