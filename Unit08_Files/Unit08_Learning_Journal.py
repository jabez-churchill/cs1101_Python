# import os
# Modify your program from Learning Journal Unit 7 to read dictionary items
# from a file and write the inverted dictionary to a file.

# How to format each dictionary item as a text string in the input file.
# How to covert each input string into a dictionary item.
# How to format each item of your inverted dictionary as a text string in the output file.


# One interpretation of the directions... as literally as possible.
def invert_dict_from_file():
    """Copy a dictionary item from a text file, inverts, then writes
    inverted dictionary to output text file."""
    imported_dict = eval(open('input01.txt').read())  # Evaluate dict from file.
    inverted = invert_dict2(imported_dict)  # Incorporate function from Unit 7.
    fout = open('output01.txt', 'w')  # Open / create output txt file.
    fout.write(str(inverted))  # Store inverted dict to output txt file.


def invert_dict2(d):
    inverse = dict()  # Declare new local dict
    for key in d:  # For each key
        val = d[key]  # Local variable saves KEY name
        for list in val:  # For each item in list value...
            if list not in inverse:  # If key name not in new dict...
                inverse[list] = key  # Create new, val (keyname) and key (value)
            else:
                inverse[list].append(key)  # Add to existing.
    return inverse


invert_dict_from_file()


def invert_verbose_dict():
    """Takes a dictionary style formatted text document, converts to
    python dict, writes formatted text to output file."""
    fin = open('input02.txt')  # Open input file.
    fout = open('output02.txt', 'w')  # Open / create output file.
    new_dict = dict()  # Declare a new dictionary.
    # Copy lines to populate new dictionary
    for line in fin:
        this_line = line.replace(' ', '').rstrip("\n")  # Reformat text
        index_pos = this_line.find('=')  # Identify index position of separator
        new_dict.update({this_line[:index_pos]: this_line[index_pos+1:]})
    inverse_dict = invert_dict(new_dict)  # Invert dictionary
    # Write lines in reverse order to output02
    for key, value in inverse_dict.items():
        # print(key, str(value[0]))
        fout.write(str('%s = %s \n' % (key, value[0])))
    print("Inverse completed.")


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


invert_verbose_dict()
