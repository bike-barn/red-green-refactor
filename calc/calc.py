"""
The calc module provides the :class:`Calc` class, which is the primary
calculator class. It contains the logic necessary to tokenize input strings and
produce a result.
"""

from .token import Token, INTEGER, EOF, PLUS


class CalcError(Exception):
    """
    The base exception for the calculator.

    Exceptions in Python inherit from :class:`Exception` and can then be used
    with the ``raise`` keyword. For example, to raise this exception one might
    do something liket this

    >>> raise CalcError("Could not parse token at position 0")
    """


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
        self.text = text
        self.position = position
        self.current_token = current_token

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
            This method is prefixed by a ``_`` to denote that it is a "private"
            method. Python itself has no concept of public or private class
            attributes or methods, but a single or double ``_`` prefix is used
            as a convention among Pythonistas to denote something that should
            not be relied upon by an external user.
        """
        text = self.text
        position = self.position

        # Check to make sure we haven't run out of characters. If we have,
        # return an EOF token.
        if position > len(text) - 1:
            # Saved by the test: Forgot this return and tests caught it.
            return Token(EOF, None)

        # Get the character that's at the current position.
        current_character = text[position]

        if current_character.isdigit():
            self.position += 1
            return Token(INTEGER, int(current_character))

        if current_character == "+":
            self.position += 1
            return Token(PLUS, current_character)

        raise CalcError(
            "Invalid token at position "
            "{position}".format(position=self.position))

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
            This method is prefixed by a ``_`` to denote that it is a "private"
            method. See the docstring for ``_next_token`` for more information.
        """
        if self.current_token.type == token_type:
            self.current_token = self._next_token()
        else:
            raise CalcError(
                "Expected {token_type} at position {position}, found "
                "{current_token}".format(token_type=token_type,
                                         position=self.position,
                                         current_token=self.current_token.type))

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
        # Just take whatever the first token is.
        self.current_token = self._next_token()

        # We expect that the first token was an integer.
        left = self.current_token
        self._consume_token(INTEGER)

        # The next expected token is a PLUS
        self._consume_token(PLUS)

        # We expect another integer for addition to work.
        right = self.current_token
        self._consume_token(INTEGER)

        # Finally, we expect to run out of input.
        self._consume_token(EOF)

        # Since we now have INTEGER PLUS INTEGER we can add both integer
        # values together.
        result = left.value + right.value
        return result
