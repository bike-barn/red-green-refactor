"""
The token module provides the :class:`Token` class, which is used to represent
various expected states in the input text for a calculator.
"""

# Saved by the test: When these constants were defined the token strings were
# inadvertently switched. The ``test_eof_token_at_end_of_line`` test caught the
# error.
INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, TIMES, DIVIDED_BY = "PLUS", "MINUS", "TIMES", "DIVIDED_BY"


# Rabbit Hole: Pylint is a program that takes in as input a Python file. It'll
#              will give you a list of syntatic, symantic, and stylistic errors
#              that you can fix. This is how you tell pylint to ignore a style
#              error if you don't agree with the style for specific instances.

# pylint: disable=too-few-public-methods
class Token:
    """
    A calculator token used to represent the current state of the calculator.

    Note:
        There is no verification of valid tokens at this point. Later versions
        of this class should verify correct input parameters.


    Attributes:
        type (str): The type of token. Valid types are currently ``INTEGER``,
            ``PLUS``, and ``EOF``.
        value (:obj:`int` or :obj:`str`): The value of the token. Valid values
            are currently non-negative integers, or the ``+`` operator.

    Rabbit hole:
        The ``type`` keyword is a reserved word in Python. It is typically bad
        practice to create a new variable that overrides a reserved word, but
        it is useful in this context and the scope is limited, so we take
        advantage of that here.
    """

    # pylint: disable=redefined-builtin
    def __init__(self, type, value):
        """Sets the type and value attributes for the Token class.

        Args:
            type (str):
                The type of token. Valid types are currently ``INTEGER``,
                ``PLUS``, and ``EOF``.
            value (:obj:`int` or :obj:`str`):
                The value of the token. Valid values are currently non-negative
                integers, or the ``+`` operator.

        # Rabbit Hole:
            In Python you can have no explicit return statement in a fucntion
            or method. These functions will return the object `None` at the end
            of their normal execution path.
        """
        self.type = type
        self.value = value

    def __str__(self):
        """
        Produce a human readable representation of this object.

        Rabbit hole:
            Methods like ``__str__`` or ``__init__`` are special methods for
            Python classes. Commonly referred to as "magic methods", these
            methods are invoked by certain Python syntax. For example, when one
            calls

            >>> str(Token('INTEGER', 3))
            Token(type=INTEGER, value=3)

            Python is actually calling the ``Token.__str__`` method to
            determine how it should create the string representation of that
            object.
        """
        return "Token(type={type}, value={value})".format(
            type=self.type,
            value=self.value,
        )
