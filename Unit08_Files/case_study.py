fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')


fin.readline()

line = fin.readline()
word = line.strip()
word

# for loop to print each line
for line in fin:
    word = line.strip()
    print(word)


# Exercise 9.1. Write a program that reads words.txt and prints only the words
# with more than 20 characters (not counting whitespace).

def exercise9_1():
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)


exercise9_1()


# Exercise 9.2. Write a function called has_no_e that returns True if the
# given word doesn’t have the letter “e” in it.

def exercise9_2prep():
    for line in fin:
        word = line.strip()
        for letter in word:
            has_e = False
            # Check if word has an e
            if letter == "e":
                has_e = True
                break
            else:
                continue
        if not has_e:
            print(word)


def has_no_e(word):
    """Iterates through letters of a word from argument, returns True if
    has e, False if no e"""
    for letter in word:
        if letter == 'e':
            return True
    return False


# # Tests
# has_no_e("Fool")
# has_no_e("Feel")


def exercise9_2():
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            continue
        else:
            print(word)


fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')
exercise9_2()


# Exercise 9.3. Write a function named avoids that takes a word and a string of
# forbidden letters, and that returns True if the word doesn’t use any of
# the forbidden letters.

def exercise9_3():
    forbidden = input("Type all forbidden letters:  ")
    forbidden_list = list(forbidden)
    words_without = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden_list):
            continue
        else:
            words_without += 1
    print(words_without)


def avoids(word, forbidden_list):
    for letter in word:
        if letter in forbidden_list:
            return True
    return False


fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')
exercise9_3()


# Exercise 9.4. Write a function named uses_only that takes a word and a string
# of letters, and that returns True if the word contains only letters in the
# list. Can you make a sentence using only the letters acefhlo?

def uses_only(word, only_letters):
    only = list(only_letters)
    for letter in word:
        if letter not in only:
            return False
    return True


# # test
# uses_only("frank", "acefhlo")


def exercise9_4():
    for line in fin:
        word = line.strip()
        if uses_only(word, "acefhlo"):
            print(word)


fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')
exercise9_4()
# cool aloe
# coal loaf


# Exercise 9.5. Write a function named uses_all that takes a word and a string
# of required letters, and that returns True if the word uses all the required
# letters at least once. How many words are there that use all the vowels
# aeiou? How about aeiouy?

def uses_all(word, required):
    all_required = list(required)
    for letter in word:
        if letter in all_required:
            all_required.remove(letter)
    if len(all_required) == 0:
        return True
    else:
        return False


# # Tests
# uses_all("maniac", "aeiouy")

def exercise9_5():
    for line in fin:
        word = line.strip()
        if uses_all(word, "aeiouy"):
            print(word)


fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')
exercise9_5()


# Exercise 9.6. Write a function called is_abecedarian that returns True if
# the letters in a word appear in alphabetical order (double letters are ok).
# How many abecedarian words are there?
def is_abecedarian(word):
    last_letter = ' '  # Starting comparison
    for letter in word:
        if letter < last_letter:
            return False
        last_letter = letter
    return True


# # Tests
# is_abecedarian("efgha")
# # False
# is_abecedarian("abcdz")
# # True

def exercise9_6():
    abecedarian_list = []
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            abecedarian_list.append(word)
    print(len(abecedarian_list))


fin = open('/Users/aaronious/github/cs1101/Unit08_Files/words.txt')
exercise9_6()
# 596
