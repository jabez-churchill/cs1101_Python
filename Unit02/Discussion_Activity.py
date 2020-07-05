# Example 1:
# Define a function that takes an argument. Call the function.
# Identify what code is the argument and what code is the parameter.


def le_taunter ( anim, food ):
    """Generates a custom Monty Python insult, requires input of one animal and one food."""
                # anim & food are both Parameters. These are variables the function, required to return a value.

    a = ("I fart in your general direction! ")
    b = ("Your mother was a " + anim + " and your father smelt of " + food + "!")
    return (a + b)

print(le_taunter("hamster", "elderberries"))
                # hamster and elderberries are the Arguments, passed into the function as required parameters.



# Example 2:
# Call your function from Example 1 three times with different kinds of arguments:
# a value, a variable, and an expression. Identify which kind of argument is which.


print(le_taunter("Nerf Herder", "Bantha"))
                        #Nerf Herder & Bantha are Values. We pass direct string objects into the parameters.


animaltype = "parrot"
foodtype = "sourdough"

print(le_taunter( animaltype, foodtype))
                        # animaltype & foodtype are both variables declared before calling the function.


print(le_taunter(str(len("fish")) + " foot tall badger", "septic snowcones"))
                # str(len("fish")) + " foot tall chipmunk" is an expression which first, gets the character length of "fish" as an integer, then converts this integer to a string, and finally connects the two strings to form a sentince.




# Example 3:
# Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results#.


def machine_goes(sound):
    s = sound
    full_sentence = "This is the machine that goes " + s
    return full_sentence

machine_goes("Whing!")

'This is the machine that goes Whing!'


#Try to call the variable inside this function:
print(s)


#Try to call the return value of this function:
print(full_sentence)


# NameError: name 'full_sentence' is not defined
# Any variable declared inside of a function can only be accessed or updated within that function. Downey (2015) uses comforatbly familiar term "Local" (p. 23) to describe variables within functions.
# Statements inside of a function may utilize a local variable that's already been declared in any line above it, such is the Flow Of Execution. Variables declared outside of the function however, can be used in statements within a function.
# This confused me in the past, seeing conventions such as "i" in for loops. This principle shows how many functions can be running at the same time which all contain commonly named variables.



# Example 4:
# Create a function that takes an argument. Give the function parameter a unique name.
# Show what happens when you try to use that parameter name outside the function. Explain the results.

def ourside_in(y):
	y = 2
	return y


# Evalulate the value of variable "y" we declared in the function.
y
# NameError: name 'y' is not defined


def inside_out(x = 1):
	return x

# Evalulate the value of variable "x" from the function, after giving it a default value.
x
#NameError: name 'x' is not defined

# Parameters work like variables, and just as in Example 3 above, are inaccessable outside of the function itself. Tested assigning a value to a parameter within a function, and also assigning a default value to a parameter (known also as a Keyword Argument). the Trying to call a parameter value outside of it's function results in a NameError, since the interpreter recognizes this a an undefined variable.
## Non-Default (Required) Argument VS Default (Keyword) Arguments = Non-Default Argument MUST come before a Default Argument


##Example 5:
##Show what happens when a variable defined outside a function has the same name as a local variable inside a function.
##Explain what happens to the value of each variable as the program runs.

#Example 5A

>>> i = 5           # Declare variable "i", assign value of 5
>>> def newi ():    # Define a new function called "newi"
	i = 10      # Statement assigns value of 10 to variable "i"
	return i    # Return value is value of variable "i"


>>> i               # Evaluate the variable "i"
5                   # The value of "i" is "5"

>>> newi()          # Call the function "newi()" which returns the value of the local variable "i".
10                  # The value of the local variable "i" is "10"

>>> i == new()      # Conditional statement to check if "i" (external) is equal to "i" (internal).
False               # The value of "i" (external) is not equal to "i" (internal).

The value of the variable "i" outside the function was not updated by the statement updating the local variable "i" within the function.

# Example 5B

>>> myText = "Outside"      # Declare a variable named "myText" and assign string value of "Outside"
>>> def check_var ():       # Create a new function called "check_var"
	myText = "Inside"   # Declare a local variable "myText" and assign value of "Inside". New variable, not an update!
	return myText       # Return the value of this new local variable "myText"

>>> myText                      # Evaluate the variable "myText".
'Outside'                       # 'Outside' value shows that the function did NOT update this variable.
>>> myText = "Still Outside!"   # Assign value of "Still Outside!" to the variable named "myText".
>>> check_var()                 # Call the "check_var" function to see if we updated the local "myText" variable inside it.
'Inside'                        # Confirmed that the local variable was not updated from outside!

I declared a variable called "i" and assigned it a value of 5. Then, created a function that includes a variable with the same name of "i", and assined it a value of 10. The function didn't update the "i" variable declared outside of the function. Results below.
