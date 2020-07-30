# char00 = dict(user_name="", gender="", age=0)


char01 = {"user_name": "Aaron", "gender": "Male", "age": 38}
char02 = dict(user_name="Bee", gender="Female", age=27)
char03 = dict(user_name="Orion", gender="Male", age=11)
char04 = dict(user_name="Airin", gender="Female", age=10)
char05 = dict(user_name="Arthur", gender="Male", age=1)


character_list = [char01, char02, char03, char04, char05]


def character_ages(chars):
    for i in chars:
        print(i["user_name"], 'is', i["age"])


# character_ages(character_list)


def show_keys(dicts):
    for i in dicts:
        for key in i.keys():
            value = i[key]
            print(key, '=', value)
        print("")


# show_keys(character_list)


eng2thai = dict()

eng2thai['one'] = 'neung'
eng2thai['two'] = 'song'
eng2thai['three'] = 'sam'
eng2thai['four'] = 'si'
eng2thai['five'] = 'ha'

# Dict Constructor
comic_universe = dict(
    Superman='DC',
    Batman='DC',
    Ironman='Marvel',
    Spawn='Dark Horse',
    BlackPanther='Marvel'

)

# Check if value is in...
'Marvel' in comic_universe.values()

# Check if key is in...
'Superman' in comic_universe.keys()


# Histogram
def histogram(iterable_object):
    d = dict()
    for one_item in iterable_object:  # for EACH in ITERABLE
        if one_item not in iterable_object:  # Not in dict yet
            d[one_item] = 1  # Add one to new key
        else:
            d[one_item] += 1  # Increment existing key
    return d


histogram('chronic')
# {'c': 2, 'h': 1, 'r': 1, 'o': 1, 'n': 1, 'i': 1}

histogram(comic_universe.values())
# {'DC': 2, 'Marvel': 2, 'Dark Horse': 1}
