my_list = [1, 2, 3, 4, 5]


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
