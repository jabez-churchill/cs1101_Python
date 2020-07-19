# EXAMPLE ONE:
# String slices can take a negative integer as an argument to index a String
# in reverse, starting from the end.

channel = ('CNN', 'Fox News', 'MSNBC', 'Al Jazerra', 'BBC World News', 'Newsy')


def add_network(channels):
    """Adds 'Network' or 'News Network' to the end of channels names
    from list, passed in as argument. """
    for i in channels:
        if i[-4:] == 'News':  # [-4:] are the last four characters of a string
            i = i + ' Network'
        else:
            i = i + ' News Network'
        print(i)


# OUTPUT:
add_network(channel)
# CNN News Network
# Fox News Network
# MSNBC News Network
# Al Jazerra News Network
# BBC World News Network
# Newsy News Network


# EXAMPLE TWO:
# String slices can skip items / places in "steps", by 2's or 3's for example.

def abbreviate(name):
    result = name[::2].replace(' ', '')  # Skip every other letter, 2 steps
    print(result)


# OUTPUT:
abbreviate('Jabez Aaron Churchill')
# JbzArnCucil
