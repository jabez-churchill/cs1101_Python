def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2."""
    return num1 / num2


def floordiv(num1, num2):
    """Returns num1 divided by num2 with remainder."""
    divided = num1 // num2
    remainder = num1 % num2
    if(remainder != 0):
        return divided, "with remainder ", remainder
    else:
        return("")


def main():
    num1 = int(input("What's number 1? "))
    num2 = int(input("What's number 2? "))
    operation = input("What do you want to do? (add, subtract, multiply, divide) ")
    if(operation == 'add'):
        print("Added", add(num1, num2))
    elif(operation == 'subtract'):
        print("Subtracted", sub(num1, num2))
    elif(operation == 'multiply'):
        print("Multiplied", mul(num1, num2))
    elif(operation == 'divide'):
        print("Divided", div(num1, num2))
        print(floordiv(num1, num2))
    else:
        print("Response not understood")
        main()


main()
