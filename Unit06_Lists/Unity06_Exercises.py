from random import randint


directions = ['forward', 'backward', 'right', 'left']


def random_direction(lis):
    direction = lis[randint(0, len(lis)-1)]
    return direction


# TEST
random_direction(directions)


# Iterate through list
def view_list():
    for direction in directions:
        print(direction)


# TEST
view_list()


# Range usage
def capitalize_list(lis):
    for i in range(len(lis)):
        # print(lis[i])
        lis[i] = lis[i].capitalize()
        print(lis[i])


# TEST
capitalize_list(directions)


nums = [2, 4, 6, 8]


def add_em_up(list):
    count = 0  # Accumulator
    for i in list:
        if type(i) != int:
            print('List can only contain numbers.')
            return
        count += i
        print('plus', i, 'is', count)
    print(sum(list), 'evaluated with sum()')
    return count


# TEST
add_em_up(nums)
add_em_up(directions)
