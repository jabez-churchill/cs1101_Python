# Finally, create your own example of a function that modifies a list passed in
# as an argument. Describe what your function does in terms of arguments,
# parameters, objects, and references.

# First, initialize a list object, containing string values of email addresses.
user_input = ['aaron@rebellious.app', 'bee', 'orion@outlook.com', 'airin@icloud.com', 'arthur@gmail.com']
user_myorg = []


def myorg_update(mail):
    new_org = '@rebellious.app'  # This will be a new
    for i in range(len(mail)):  # For loop to iterate through each value.
        if mail[i].__contains__("@"):
            at = mail[i].find('@')  # Use find method to record index of '@'
            outside_org = mail[i]  # Temporary variable to access string index.
            mail[i] = outside_org[:at] + new_org  # Assign
        else:
            mail[i] += new_org
        print(mail[i])
    return


user_myorg = user_input[:]  # Object user_email is COPIED to object user_myorg
myorg_update(user_myorg)  # Call the above function to reformat emails.


def get_input():
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
        myorg_update(user_myorg)
        get_input()
    elif operation == 2:
        new_user = input("Please enter an email or username:  ")
        user_input.append(new_user)
        myorg_update(user_input)
        print("")
        get_input()
    elif operation == 3:
        print("Which user would you like to delete? ")
        for i in user_input:
            counter = 0
            print(counter, i)
            counter += 1
        delete_num = int(input("Delete user number: "))
        # Guardian
        x = user_input.pop(delete_num)
        print("")
        print("User", x, "deleted.")
        get_input()
    else:
        return


get_input()
