# Describe how tuples can be useful with loops over lists and dictionaries
#
# Tuples are useful with lists and dictionaries to utilize values from two
# separate iterable objects, using the zip function. Zip can be used to create
# a new list, dictionary, set of tuples, do comparisons, or other functions.
# The items method seems like a great way to utilize both (well named) keys and
# associated values. Tuples are the return type of items() method.

# Create a dictionary
marvel_heroes = {
    "Silver Surfer": 1966,
    "Moon Knight": 1975,
    "Black Panther": 1966,
    "Cyclops": 1963,
    "Deadpool": 1991,
    "Iron Man": 1963,
    "The Punisher": 1974,
    "Storm": 1975,
    "Wolverine": 1974,

}
# Create a list
dc_heroes = ["Superman", "Supergirl", "Batman", "Batgirl", "Aquaman", "Wonder Woman"]
# Create a tuple
weapons = ("Water Balloons", "Nerf Guns", "Pillows", "Dance Battle", "Insults", "Drinking Games")

# Zip Method
# Here, I can uzilize values from three different objects of different types.
# I'm using the first dictionary, a list, and a tuple.


def challenges(team1, team2):
    # global weapons
    for trio in zip(team1, team2, weapons):
        print(trio[0], "vs", trio[1], "with", trio[2])


print("_"*79)
print("Demonstration of the zip() method.")
challenges(marvel_heroes, dc_heroes)


# Items Method
# The items() method returns a list [] of tuples (,) called dict_items. These
# are predicable and easy to use one, the other, or both values.
def only70s(heroes):
    for hero, year in heroes.items():
        if year >= 1970 and year < 1980:  # We can uzilize the value, key, or
            if hero == 'Wolverine':  # both value & key for differring reasons.
                print('Snikt!')
            print(hero, year)


print("_"*79)
print("Demonstration of the items() method. 70's heros only.")
only70s(marvel_heroes)

# Your descriptions and examples should include the following: the zip
# function, the enumerate function, and the items method.


# Enumerate Method
def list_heroes(heroes):
    for index, name in enumerate(heroes):
        print(index, name)


print("_"*79)
print("Demonstration of the enumerate() method.")
list_heroes(marvel_heroes)
print(list(enumerate(dc_heroes)))
()
