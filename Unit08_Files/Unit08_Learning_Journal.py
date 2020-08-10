# Modify your program from Learning Journal Unit 7 to read dictionary items
# from a file and write the inverted dictionary to a file.


# EXAMPLE ONE
# One interpretation of the directions... as literally as possible.
def invert_dict_from_file():
    """Imports a dictionary OBJECT from a text file, inverts, then writes
    inverted dictionary to output text file."""

    imported_dict = eval(open('input01.txt').read())  # Evaluate dict from file.
    inverted = invert_dict2(imported_dict)  # Incorporate function from Unit 7.
    fout = open('output01.txt', 'w')  # Open / create output txt file.
    fout.write(str(inverted))  # Store inverted dict to output txt file.
    print("Inverse completed: output01.txt")


def invert_dict2(d):
    inverse = dict()  # Declare new local dict
    for key in d:  # For each key
        val = d[key]  # Local variable saves KEY name
        for list in val:  # For each item in value list...
            if list not in inverse:  # If key name not in new dict...
                inverse[list] = key  # Create new, val (keyname) and key (value)
            else:
                inverse[list].append(key)  # Add to existing.
    return inverse


invert_dict_from_file()


# EXAMPLE TWO
# Another interpretation of the directions. I invert both the item order, plus
# the key/value positions. The input and output files are formatted text.
def invert_verbose_dict():
    """Takes a dictionary style formatted text document,
    inverts order of keys/values and order of items,
    writes formatted text to output file."""

    fin = open('input02.txt')  # Open input file.
    fout = open('output02.txt', 'w')  # Open / create output file.
    new_dict = dict()  # Declare a new dictionary.

    # Copy lines to populate new dictionary
    for line in fin:
        this_line = line.replace(' ', '').rstrip("\n")  # Reformat text
        index_pos = this_line.find('=')  # Identify index position of separator
        new_dict.update({this_line[:index_pos]: this_line[index_pos+1:]})

    # Write each to file.
    i = len(new_dict)-1
    keys = list(new_dict.keys())  # Convert keys to list to access by index.
    vals = list(new_dict.values())  # Convert values to list to access by index.
    while i >= 0:
        # fout.write(str('%s = %s \n' % (vals[i], keys[i])))  # Format operator!
        fout.write('%s = %s \n' % (vals[i], keys[i]))  # Format operator!

        i -= 1
    print("Inverse completed: output02.txt")


invert_verbose_dict()
