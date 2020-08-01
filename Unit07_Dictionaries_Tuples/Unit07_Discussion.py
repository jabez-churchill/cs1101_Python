# Describe how tuples can be useful with loops over lists and dictionaries

# The dictionaries list() method is one useful way to utilze tuples and loops.
# A two-value tuple is the return value of the items() method for dictionaries.
# The items method seems like a great way to utilize both (well named) keys and
# associated values.

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

# The items() method returns a list [] of tuples (,) called dict_items.
marvel_heroes.items()
# dict_items([('Silver Surfer', 1966), ('Captain Marvel', 1968), ('Spider-Man',
# 1963), ('Wolverine', 1974), ('Moon Knight', 1975), ('Black Panther', 1966),
# ('Cyclops', 1963), ('Deadpool', 1991), ('Iron Man', 1963), ('The Punisher',
# 1974), ('Storm', 1975)])


def only70s(heroes):
    for hero, year in heroes.items():
        if year >= 1970 and year < 1980:  # We can uzilize the value, key, or
            if hero == 'Wolverine':  # both value & key for differring reasons.
                print('Snikt!')
            print(hero, year)


only70s(marvel_heroes)
