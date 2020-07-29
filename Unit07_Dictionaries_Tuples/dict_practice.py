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


character_ages(character_list)


def show_keys(dicts):
    for i in dicts:
        for key in i.keys():
            value = i[key]
            print(key, '=', value)
        print("")


show_keys(character_list)
