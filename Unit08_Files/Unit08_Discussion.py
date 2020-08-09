import os
# Describe how catching exceptions can help with file errors. Write three
# Python examples that actually generate file errors on your computer and
# catch the errors with try: except: blocks. Include the code and output
# for each example in your post.


# EXAMPLE ONE
# When i try to open a file that doesn't exist, the execpt clause catches the
# error, informs me, and gives me another chance by recursing instead of end.
def try_file():
    file_name = input("Enter name of file to open: ")
    try:
        fout = open(file_name)
        print(file_name, 'opened successfully.')
    except:
        print("File not found. Please try again.")
        try_file()


try_file()
# Enter name of file to open: output.rtf
# File not found. Please try again.
# Enter name of file to open: output.txt
# output.txt opened successfully.


# EXAMPLE TWO
# Catching errors with and try / except blocks can give specific directions
# to handle the error, or try to automatically fix it.
def select_file():
    file_name = input("Enter name of file to open: ")
    try:
        open(file_name)
        print(file_name, 'opened successfully.')
    except:
        print("File not in current directory. \nCurrent dir includes:")
        files_here = os.listdir()
        for item in files_here:
            if item[0] != "." and os.path.isfile(item):
                print(item)
        select_file()


# Output:
select_file()
# Enter name of file to open: nerd.txt
# File not in current directory.
# Current dir includes:
# captions.db
# output.txt
# Enter name of file to open: output.txt
# output.txt opened successfully.


# EXAMPLE THREE
# We can specify the type of error to react to, to make error messages more
# useful in identifying or resolving problems.
def open_something(to_open):
    try:
        cwd = os.getcwd()
        open(cwd + "/" + to_open, "r")
    except IsADirectoryError:
        print("Can't open directory as file.")


# Output:
open_something('github')
# Can't open directory as file.
