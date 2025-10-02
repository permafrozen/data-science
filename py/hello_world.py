# Script to practise python
__author__ = "Royale King"
__version__ = "1.0"

from prompt_toolkit.shortcuts import clear


# Ctrl+F8 -> toggle breakpoint.
# Shift+f10 -> Run Script

def print_hi(string):
    print(f"What's good? I'm {string}!")

# If script executed by py interpreter __name__ == __main__
if __name__ == '__main__':
    print_hi(__name__)
    print("Hello", 'World', sep=" ", end="!\n")

    """
    var allocation & Datatypes
    """

    name = "Mazda"
    model = str("RX-7")
    year = 1985
    price = float(9000)

    # formated string
    print("The %s %s was built %d and costs %.2f€" % (name, model, year, price))
    print(f"Hello, I'm a year and I'm a {type(year)}")

    notString = 6, 7, "Yo I'm a tuple"
    print(notString[0], notString[1], notString[2])

    im_false = False
    im_true = bool(1)

    if im_false != im_true:
        print("I am inside an if")
