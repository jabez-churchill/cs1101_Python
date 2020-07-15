import random

my_anims = ["owl", "deer", "seal", "cat", "hawk"]


def while_on(n=0):
    while n < len(my_anims):
        print('I like', my_anims[n] + 's')
        n += 1


while_on()


# Exercise 7.3
# rewrite the function print_n from Section 5.8
# using iteration instead of recursion.
def print_n(s, n):
    if n <= 0:
        return
    print(s, n)
    print_n(s, n-1)


def print_n2(s, n):
    while n > 0:
        print(s, n)
        n -= 1


print_n("count", 5)
print_n2("count", 5)


# Breaks

while True:
    input("Press Enter To Roll")
    print(random.randrange(1, 7))
