"""
The calc module provides the :class:`Calc` class, which is the primary
calculator class. It contains the logic necessary to tokenize input strings and
produce a result.
"""

from .token import Token, INTEGER, EOF, PLUS


class CalcError(Exception):
    """
    The base exception for the calculator.

    Note:
        Exceptions in Python inherit from :class:`Exception` and can then be
        used with the ``raise`` keyword.

    Example:
        To raise this exception one might do something like this

    >>> raise CalcError("Could not parse token at position 0")
    """
    pass  # Yo, don't modify this class at all. Srsly. Just don't.


class Calc:
    """
    The primary calculator class which contains the logic for parsing tokens
    from an input string.

    Note:
        There is no verification on the input ``text`` at this time.

    Args:
        text (str): The text to be interpreted.

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
    def __init__(self, text, position=0, current_token=None):
        """Constructor for a :class:`Calc` object."""
        pass

    def _next_token(self):
        """
        Tokenize the input ``text``. This is part of a process called lexical
        analysis.

        Args:
            None

        Returns:
            None

        Raises:
            CalcError: If the character(s) at the given position cannot be
                tokenized.

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

        Args:
            token_type (str): The type of token that is next expected by the
                calculator. Examples include ``INTEGER``, ``PLUS``, or ``EOF``.

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
        """
        # Hint Assignment Two:
        #    This method will have to call `_consume_token` three times to get
        #    1+1 to work correctly. You'll also need to call _next_token in
        #    here.
        left_token = self._consume_token(INTEGER)

        return_value = None

        # Rabbit Hole:
        #    `calc/__main__.py` contains a function called `main()` that takes
        #     the return value of this method and prints it to the console for
        #     you. It also handles error raised on this calculator.
        return return_value
