list1 = [1, 3, 5, 7, 9]
list2 = []
list3 = []


def make_alias(l1, l2):
    l2 = l1
    l3 = l1[:]
    l2.append(2)
    l3.append(4)
    print('list1 is', l1)
    print('list2 is', l2)
    print('list2 is', l3)
    print('list1 is list2', l1 is l2)
    print('list1 is list3', l1 is l3)


make_alias(list1, list2)
