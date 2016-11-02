"""
The calc module provides the :class:`Calc` class, which is the primary
calculator class. It contains the logic necessary to tokenize input strings and
produce a result.
"""

from calc.token import Token, INTEGER, EOF, PLUS, MINUS, TIMES, DIVIDED_BY


class CalcError(Exception):
    """
    The base exception for the calculator.

    Exceptions in Python inherit from :class:`Exception` and can then be used
    with the ``raise`` keyword. For example, to raise this exception one might
    do something like this

    >>> raise CalcError("Could not parse token at position 0")
    """
    pass  # Yo, don't modify this class at all. Srsly. Just don't.


# Rabbit Hole:
#   Pylint is a program that takes in as input a Python file. It'll will give
#   you a list of syntatic, semantic, and stylistic errors that you can fix.
#   This is how you tell pylint to ignore a style error if you don't agree with
#   the style for specific instances.

# pylint: disable=too-few-public-methods
class Calc:
    """
    The primary calculator class which contains the logic for parsing tokens
    from an input string.

    Note:
        There is no verification on the input ``text`` at this time.

    Attributes:
        text (str): The text to be interpreted.
        position (int): The current position of the interpreter. Used as an
            index into a :obj:`str`, ``text``. Defaults to ``0``, the beginning
            of the input ``text``.
        current_token (Token): The current :class:`Token` being evaluated by the
            intepreter. Defaults to ``None`` as initially no :class:`Token`s
            have been parsed.

    Example:

    >>> calc = Calc("3+4")
    >>> calc.parse()
    7

    """
    # Rabbit Hole:
    #    You can read the position=0 syntax as saying "The default argument,
    #    if you don't pass an argument to this function, is the value on the
    #    right.
    def __init__(self, text, position=0, current_token=None):
        """Set's the ``text``, ``position``, and ``current_token`` attributes
        for the ``Calc`` class.

        Args:
        text (str): The text to be interpreted.
        position (int):
            The current position of the interpreter. Used as an index into a
            :obj:`str`, ``text``. Defaults to ``0``, the beginning of the input
            ``text``.
        current_token (Token):
            The current :class:`Token` being evaluated by the intepreter.
            Defaults to ``None`` as initially no :class:`Token`s have been
            parsed.

        Returns:
            None

        Raises:
            None
        """
        pass

    def _next_token(self):
        """
        This function looks at a single character (for now) and checks if this
        is a known character or not. If it's a known character, like '+' for
        example, it will return a Token of type PLUS with a value of None.

        NOTE: This function may advance `self.position`.

        Args:
            None

        Returns:
            A Token

        Raises:
            CalcError: If the current character is not a known token type.

        Hint Assignment Two:
            If you're struggling for how to match integers look up Python's
            str.isdigit().

        Rabbit hole:
            The name of this method is prefixed by a ``_`` to denote that it is
            a "private" method. Python itself has no concept of public or
            private class attributes or methods, but a single or double ``_``
            prefix is used as a convention among Pythonistas to denote something
            that should not be relied upon by an external user.
        """
        pass

    def _consume_token(self, token_type):
        """
        Ensure that the current token type matches the given ``token_type``. If
        it does, set the current token to be the next token, effectively
        consuming a token.

        NOTE:
            This function replaces `self.current_token` but does not modify
            `self.position`.

        Args:
            matching_tokens (list[str]): The types of tokens that is next
            expected by the calculator.

            Examples include ``INTEGER``, ``PLUS``, or ``EOF``.

        Returns:
            None

        Raises:
            CalcError: If ``token_type`` does not match the current token.

        Rabbit hole:
            The name of this method is prefixed by a ``_`` to denote that it is
            a "private" method. See the docstring for ``_next_token`` for more
            information.
        """
        pass

    def parse(self):
        """
        Attempt to consume all tokens found in the input text.

        These tokens are expected to be found in a certain order, otherwise
        known as a grammar.  The current grammar (or set of rules for allowable
        tokens) looks like

        INTEGER PLUS INTEGER

        All other combinations are not currently supported.

        Args:
            None

        Returns:
            result (int): The numeric result of parsing the input text as a set
                of arithmetic operations.

        Raises:
            CalcError: If an invalide operator is found.

        Hint Assignment Two:
            Start with me!

        MORE Hint Assignment Two:
            This method will have to call `_consume_token` three times to get
            1+1 to work correctly. You'll also need to call _next_token in
            here.
        """
        left_token = self._consume_token(INTEGER)

        return_value = None

        # Rabbit Hole:
        #    `calc/__main__.py` contains a function called `main()` that takes
        #     the return value of this method and prints it to the console for
        #     you. It also handles error raised on this calculator.
        return return_value
