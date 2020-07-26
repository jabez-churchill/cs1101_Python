# Finally, create your own example of a function that modifies a list passed in
# as an argument. Describe what your function does in terms of arguments,
# parameters, objects, and references.

# First, initialize a list object, containing string values of email addresses.
user_input = ['aaron@rebellious.app', 'bee', 'orion@outlook.com', 'airin@icloud.com', 'arthur@gmail.com']
user_myorg = []


def myorg_update(user, myorg):
    myorg = user[:]
    new_org = '@rebellious.app'  # This will be a new
    for i in range(len(user)):  # For loop to iterate through each value.
        if user[i].__contains__("@"):
            at = user[i].find('@')  # Use find method to record index of '@'
            outside_org = user[i]  # Temporary variable to access string index.
            myorg_email = outside_org[:at] + new_org  # Assign to new variable
        else:
            myorg_email = user[i] + new_org
        myorg.append(myorg_email)
        print(myorg[i])
    return


user_myorg = user_input[:]  # Object user_email is COPIED to object user_myorg
myorg_update(user_myorg)  # Call the above function to reformat emails.


def get_input():
    print("")
    print("Choose an option:")
    print("1. View email list.")
    print("2. Add new user to list.")
    print("3. Delete a user.")
    print("4. Exit")
    print("")
    operation = int(input("Enter your selection: "))
    if operation not in [1, 2, 3, 4]:
        print("")
        print("Only numbers between 1 - 4 are valid.")
        get_input()
    elif operation == 1:
        myorg_update(user_input, user_myorg)
        print("")
        get_input()
    elif operation == 2:
        print("")
        new_user = input("Please enter an email or username:  ")
        user_input.append(new_user)
        myorg_update(user_input, user_myorg)
        print("")
        get_input()
    elif operation == 3:
        print("")
        print("Which user would you like to delete? ")
        counter = 0
        for i in user_input:
            print(counter, i)
            counter += 1
        print("")
        delete_num = int(input("Delete user number: "))
        if delete_num not in range(1, len(user_input)):
            print("User not found.")
            print("")
            get_input()
        x = user_input.pop(delete_num)
        print("")
        print("User", x, "deleted.")
        print("")
        myorg_update(user_input, user_myorg)
        get_input()
    else:
        return


get_input()
