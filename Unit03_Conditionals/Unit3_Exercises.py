
# Exercise 3.1
print('Exercise 3.1')
print('Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.')

def right_justify(s):
    word_length = len(s)
    num_spaces = 70 - word_length
    print(" " * num_spaces + s)

print('Answer 3.1')
right_justify("Isn't it awfully nice to have a penis?")
right_justify("Isn't is frightly good to have a dong?")
right_justify("It's swell to have a stiffy,")
right_justify("it's divine to own a dick.")
right_justify("From the tiniest little tadger,")
right_justify("to the worlds biggest prick.")




# Exercise 3.2
print('Exercise 3.2')
print("A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice.")


    # 1. Type this example into a script and test it.
def do_twice(f):
    f()
    f()

def print_spam():
    print('Spam')

print('Example')
do_twice(print_spam)
print(' ')


    #2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
def mod_do_twice(func, arg):
    func(arg)
    func(arg)

    #3. Copy the definition of print_twice from earlier in this chapter to your script.
def print_twice(bruce):
    print(bruce)
    print(bruce)


    #4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as anargument.
print('Solution 3.2')
mod_do_twice(print_twice, 'spam')

    #5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_four(func, arg):
    mod_do_twice(func, arg)
    mod_do_twice(func, arg)

do_four(print, 'cool')



# Exercise 3.3
print('Exercise 3.3')
