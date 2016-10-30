"""
The token module provides the :class:`Token` class, which is used to represent
various expected states in the input text for a calculator.
"""

# Saved by the test: When these constants were defined the token strings were
# inadvertently switched. The ``test_eof_token_at_end_of_line`` test caught the
# error.
INTEGER, EOF, PLUS = 'INTEGER', 'EOF', 'PLUS'


class Token:
    """
    A calculator token used to represent the current state of the calculator.

    Note:
        There is no verification of valid tokens at this point. Later versions
        of this class should verify correct input parameters.

    Args:
        type (str): The type of token. Valid types are currently ``INTEGER``,
            ``PLUS``, and ``EOF``.
        value (:obj:`int` or :obj:`str`): The value of the token. Valid values
            are currently non-negative integers, or the ``+`` operator.

    Attributes:
        type (str): The type of token. Valid types are currently ``INTEGER``,
            ``PLUS``, and ``EOF``.
        value (:obj:`int` or :obj:`str`): The value of the token. Valid values
            are currently non-negative integers, or the ``+`` operator.

    Rabbit hole:
        The ``type`` keyword is a reserved word in Python. It is typically bad
        practice to create a new variable that overrides a reserved word, but it
        is useful in this context and the scope is limited, so we take advantage
        of that here.
    """

    def __init__(self):
        """Constructor for a :class:`Token` object."""
        pass

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

            Python is actually calling the ``Token.__str__`` method to determine
            how it should create the string representation of that object.
        """
        pass
