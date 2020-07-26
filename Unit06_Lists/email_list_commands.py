user_input = ['aaron@rebellious.app', 'bee', 'orion@outlook.com', 'airin@icloud.com', 'arthur@gmail.com']
user_myorg = []


# Sync Users
def sync_users(users, myorg):
    myorg.clear()  # Clear the email list.
    new_org = '@rebellious.app'  # This will be the new email address domain.
    for i in range(len(users)):  # For loop to iterate through each value.
        if users[i].__contains__("@"):  # If the value has an @ symbol
            at_position = users[i].find('@')  # Find method to record index of '@'
            outside_org = users[i]  # Temporary variable to access string index.
            myorg_email = outside_org[:at_position] + new_org  # Replace domain.
        else:
            myorg_email = users[i] + new_org  # Add domain to non-email format.
        myorg.append(myorg_email)  # Append new email value to user_myorg list.
    return


# Show Emails
def show_emails(users):
    for i in user_myorg:  # For each value in list
        print(i)  # Print the value


# Add User to user list
def add_user(new_name):
    user_input.append(new_name)  # Append argument as new list value.
    print_nicely(str(new_name + " added to list."))


# Delete user from user list
def delete_user(users):
    print_nicely("Which user would you like to delete? ")
    counter = 0
    for i in users:  # For each email in list.
        print(counter, i)  # Print the index number and email
        counter += 1  # Increment up
    to_remove = int(input("Delete user number:  "))
    x = users.pop(to_remove)
    print_nicely(str(x + " deleted from list."))
    return


# Print Nice Message
def print_nicely(toprint):
    """Prints a message between line breaks."""
    print("")
    print(toprint)
    print("")


# Interface
def run_program():
    print("")
    print("Choose an option:")
    print("1. View email list.")
    print("2. Add new user to list.")
    print("3. Delete a user.")
    print("4. Exit")
    print("")

    operation = int(input("Enter your selection: "))
    # Guardian
    if operation not in [1, 2, 3, 4]:  # Here's a list of possible choices.
        print_nicely("Only numbers between 1 - 4 are valid.")
        run_program()  # Start over.
    # Option 1: Show current email list.
    elif operation == 1:
        sync_users(user_input, user_myorg)
        show_emails()
        run_program()
    # Option 2: Add a new user.
    elif operation == 2:
        to_add = input("Enter new user name or email:  ")
        add_user(to_add)
        sync_users(user_input, user_myorg)
        show_emails()
        run_program()
    # Option 3: Delete a user.
    elif operation == 3:
        delete_user(user_input)
        sync_users(user_input, user_myorg)
        show_emails()
        run_program()
    # Option 4: Exit.
    else:
        print_nicely("Goodbye.")
        return


run_program()




# NOTES:
# I had first wrote one ridiculously long function that included all of these
# smaller functions, that proceed inside each fork of the interface() function.
# It was horrible, it didn't work, and I wasted an embarassing amount of time
# trying to figure out why. After breaking it into smaller functions I got it.
#
# Turned out that I was trying to make statements like list1 = list2 or
# list1 = list3[:]... but when inside of a function, the first entry was being
# read as a local variable, in either case of trying to access the list directly
# or when accessing it as an argument.
