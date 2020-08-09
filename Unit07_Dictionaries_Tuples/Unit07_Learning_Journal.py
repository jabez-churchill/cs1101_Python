# Create a Python dictionary that returns a list of values for each key.
# Here is a dictionary of gift ideas for my family members, returning lists of
# tuples, each containing the item and price.
gifts_someday = {
    ("Orion", "Churchill"): [("monitor", 120), ("graphics card", 150), ("gaming chair", 80)],
    ("Airin", "Churchill"): [("small tv", 100), ("ipad mini", 200), ("makeup kit", 75)],
    ("Arthur", "Churchill"): [("kiddy pool", 80), ("slide", 180), ("magnet set", 30)],
    ("Taniss", "Churchill"): [("ring", 200), ("seafood buffet", 100), ("spa day", 150)]
}


# Test dictionary that's easier to keep track of!
new_dict = {
    "numbers": [1, 2, 3],
    "letters": ["a", "b", "c"],
    "symbols": ["!", "@", "#"]
}


# Modify this function so that it can invert your dictionary. In particular,
# the function will need to turn each of the list items into separate keys in
# the inverted dictionary.
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


print("_"*69)
print("Original dictionary.")
print(gifts_someday)

print("_"*69)
print("Inverted dictionary.")
print(invert_dict2(gifts_someday))


# When building my dictionary, I'd envisioned this function. Checks what
# gifts I can afford by passing in my current budget.
def gift_budget(budget):
    """Search list items within the budget, passed in as an argument."""
    global gifts_someday
    for fam in gifts_someday.items():
        # within one dictionary key-value pair, including the list value
        name = fam[0]
        gifts = fam[1]
        for gift in gifts:
            if gift[1] <= budget:
                print(gift[0], "for", name[0])  # Print gift and first name.


print("_"*69)
print("Initial Idea: With a budget of $100, I can afford... gift_budget(100)")
gift_budget(100)
# gaming chair for Orion
# small tv for Airin
# makeup kit for Airin
# kiddy pool for Arthur
# magnet set for Arthur
# seafood buffet for Taniss
