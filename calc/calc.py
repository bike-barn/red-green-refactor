"""
The calc module provides the :class:`Calc` class, which is the primary
calculator class. It contains the logic necessary to tokenize input strings and
produce a result.
"""

from .token import Token, INTEGER, EOF, PLUS, MINUS, TIMES, DIVIDED_BY


class CalcError(Exception):
    """
    The base exception for the calculator.

    Exceptions in Python inherit from :class:`Exception` and can then be used
    with the ``raise`` keyword. For example, to raise this exception one might
    do something liket this

    >>> raise CalcError("Could not parse token at position 0")
    """


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

    def _tokenize_integer(self, text):
        """If have found a single digit then this helper function will read
        characters until the end of the integer is found.

        Args:
            text: A section of the text that is assumed to contain an integer

        Returns:
            Token

        Raises:
            None
        """
        # Saved By The Test:
        #   The first couple attempts at this function were very messed up and
        #   broke other functionality in the interpreter that my tests caught.

        # First we check to see if there are other digits in the int.
        first_position = self.position
        current_position = self.position
        current_character = text[current_position]

        while True:
            if not current_character.isdigit():
                break

            current_position += 1
            try:
                current_character = text[current_position]
            except IndexError:
                # If we've hit EOF we'll hit this exception.
                break

        # Current position should be EOF or a digit.
        self.position = current_position
        value = int(text[first_position: current_position])
        return Token(INTEGER, value)

    def _consume_whitespace(self, text):
        """Eats all whitespace found until there's nothing left.

        Args:
            text: The input text to have whitespace removed until a non
                  whitespace character is found.

        returns:
            None

        raises:
            None
        """
        current_position = self.position
        current_character = text[current_position]
        while True:
            if not current_character.isspace():
                break

            current_position += 1
            try:
                current_character = text[current_position]
            except IndexError:
                # If we've hit EOF we'll hit this exception.
                break

        self.position = current_position

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
        text = self.text
        position = self.position

        # Check to make sure we haven't run out of characters. If we have,
        # return an EOF token.
        if position > len(text) - 1:
            # Saved by the test: Forgot this return and tests caught it.
            return Token(EOF, None)

        # Get the character that's at the current position.
        current_character = text[position]

        # If we find whitespace eat it like we're Packman.
        if current_character.isspace():
            self._consume_whitespace(text)

            if self.position > len(text) - 1:
                return Token(EOF, None)
            # After we've eatten all the bab whitespace lets actually grab a
            # symantically meaningful character.
            current_character = text[self.position]

        # Saved By The Test: test_arithmetic caught an error if return_token
        #                    was never set
        return_token = None  # Stores the token that's been lexed.

        if current_character.isdigit():
            return_token = self._tokenize_integer(text)

        if current_character == "*":
            self.position += 1
            return_token = Token(TIMES, current_character)

        if current_character == "/":
            self.position += 1
            return_token = Token(DIVIDED_BY, current_character)

        if current_character == "+":
            self.position += 1
            return_token = Token(PLUS, current_character)

        if current_character == "-":
            self.position += 1
            return_token = Token(MINUS, current_character)

        if return_token is None:
            raise CalcError(
                "Invalid token at position "
                "{position}".format(position=self.position))

        return return_token

    def _consume_token(self, matching_tokens):
        """
        Ensure that the current token type matches the given ``token_type``. If
        it does, set the current token to be the next token, effectively
        consuming a token.

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
        if self.current_token.type in matching_tokens:
            self.current_token = self._next_token()
        else:
            raise CalcError(
                "Expected {matching_tokens} at position {position}, found "
                "{current_token}".format(matching_tokens=matching_tokens,
                                         position=self.position,
                                         current_token=self.current_token.type))

    # pylint: disable=invalid-name
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
        """
        # Just take whatever the first token is.
        self.current_token = self._next_token()

        left = self.current_token
        self._consume_token(INTEGER)

        result = None
        while True:
            op = self.current_token
            expected_operations = [PLUS, MINUS, TIMES, DIVIDED_BY]
            self._consume_token(expected_operations)

            right = self.current_token
            self._consume_token(INTEGER)

            if result is None and op.type in (TIMES, DIVIDED_BY):
                # multiplying or dividing 0 is bad times.
                result = 1

            # Since we now have INTEGER PLUS INTEGER we can add both integer
            # values together.

            # Saved By The Test:
            #    The Division if statement was originally a copy and paste
            #    of the multiplication if statement. Forgot to change the
            #    operator.

            if op.type == TIMES:
                result = left.value * right.value
            elif op.type == DIVIDED_BY:
                # Saved By The Test:
                #    This function accidently did floating point division and
                #    the unit tests cought it.
                result = left.value // right.value
            elif op.type == PLUS:
                result = left.value + right.value
            elif op.type == MINUS:
                result = left.value - right.value
            else:
                raise CalcError(
                    "Unknown Operator found at {position}".format(
                        position=self.position,
                    ))

            left = Token(INTEGER, result)

            # When we run out of input we need to check that the last token is
            # EOF.
            if self.current_token.type == EOF:
                self._consume_token(EOF)
                return result
