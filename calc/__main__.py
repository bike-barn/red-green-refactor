import traceback
from calc import Calc, CalcError


def main():
    """
    The main entry point into the ``calc`` program.

    This function takes input from the user, attempts to parse it, and either
    returns the result or shows a stack trace to make it easier to identify the
    root cause of the error.

    Args:
        None

    Returns:
        None
    """
    while True:
        # Attempt to get user input.
        try:
            text = input('calc> ')
        except EOFError:  # Allow the user to use ctrl+d to exit the calculator.
            break

        if not text:
            continue

        calc = Calc(text)
        try:
            result = calc.parse()
        except CalcError:
            traceback.print_exc()  # Show a stack trace on errors.
        else:
            print(result)

# Rabbit hole: This pattern below is a Python idiom that basically says, if this
# module (this file) is being run as the main program (i.e. it was invoked from
# the command line as python __main__.py), then run the main() function. In
# practice this means that this module can be imported without actually running
# the main() function, but that main() will be run if that is the intention.
if __name__ == '__main__':
    main()
