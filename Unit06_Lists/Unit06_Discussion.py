# Objects, Values, Is Operator
# Describe the difference between objects and values using the terms
# “equivalent” and “identical”. Illustrate the difference using your
# own examples with Python lists and the “is” operator.



actors = ['John', 'Terry', 'Graham', 'Eric', 'Michael']  # Object
humans = []  # Reference

humans = actors  # 'humans' is a variable referring to the object 'actors'

actors.append('Terry')
#
# actors
# ['John', 'Terry', 'Graham', 'Eric', 'Michael', 'Terry']
#
# humans
# ['John', 'Terry', 'Graham', 'Eric', 'Michael', 'Terry']

# To demonstrate this, we can use the 'is' operator to confirm two variables
# refer to the same object. If you update a value, the changed value will
# be reflected using both of the two variable names. The values referred to
# by both of these names, are "identical", because they are really one object.

# The 'is' operator checks whether a variable refers to an
# object or not. Returns a boolean value.
actors is humans
# True


actors = ['John', 'Terry', 'Graham', 'Eric', 'Michael']
characters = ['John', 'Terry', 'Graham', 'Eric', 'Michael']

actors is characters
# False
# Because lists have the same values, they are "equivilent" or equal. These
# two variables refer to two different objects.

characters.append('Terry')

characters
['John', 'Terry', 'Graham', 'Eric', 'Michael', 'Terry']

actors
['John', 'Terry', 'Graham', 'Eric', 'Michael']
# Even though the two object can have equivalent values, updating a value
# in one object will not update the values in the other. These are two
# different objects that can be equivalent, but they are not identical.


# Describe the relationship between objects, references, and aliasing. Again,
# create your own examples with Python lists.

# When two or more variables refer to the same object, it's called aliasing.
# In English, the word "alias" is used to describe a false name a person may
# be known by. An alias in programming is used as an indirect name of a data
# object.

list_one = [11, 10, 26, 38, 1]  # Object
reference_to_list_one = []

#  Aliasing
reference_to_list_one = list_one

list_one is reference_to_list_one
# True
# The variable reference_to_list_one is now a reference to the object list_one.



# One object may be referenced by two variables, whereas either two names
# may be used to call or update the same singular data source.

myemail = 'aaron@neato.com'

new_email = myemail.find('@')
check_email = myemail.__contains__('@rebellious')



# Finally, create your own example of a function that modifies a list passed in
# as an argument. Describe what your function does in terms of arguments,
# parameters, objects, and references.

user_email = ['aaron@rebellious.app', 'bee@rebellious.app', 'orion@outlook.com', 'airin@rebellious.app', 'arthur@gmail.com']
user_gsuite = []
user_appleid = []


def appleid_update(mail):
    new_org = '@appleid.rebellious.app'
    for i in range(len(mail)):
        if mail[i].__contains__('@rebellious'):
            mail[i] = mail[i].replace('@rebellious.app', new_org)
        else:
            at = mail[i].find('@')
            outside_org = mail[i]
            mail[i] = outside_org[:at] + new_org
    return


user_gsuite = user_email  # Aliasing, gsuite is a referrence to object user_email
user_appleid = user_email[:]  # Object user_email is copied to object user_appleid
appleid_update(user_appleid)
