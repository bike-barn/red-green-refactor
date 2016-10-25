"""This program is a interpreter for a subset of the PASCAL programming
language. It's' based off of the Let's Build A Simple Interpreter tutorial
found at https://ruslanspivak.com/lsbasi-part1/

This code base was build and tested in Python3.5.
"""

from .token import Token, INTEGER, EOF, PLUS

class CalcError(Exception):
    """Base exception for the calculator."""

class Calc:

    def __init__(self, text):
        """
        """
        # Text to be interpreted
        # NOTE: no verification at this point in time.
        self.text = text
        # position of the index on self.text
        self.position = 0
        # current token
        self.current_token = None

    def _next_token(self) -> Token:
        """This is the method that calls the token class and breaks the input
        text into a set of tokens. This set of operations is called lexical
        analyization.

        raises:
            CalcError: If the character(s) at the given position cannot be
                tokenized.
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
        """consume_token checks the current tokens type with the token type
        that's passed in. If they don't match then an error is raised.

        args:
            token_type: You can think of the token_type as the token that is
                next expected and should be found.

        raises:
            CalcError: If ``token_type`` does not match the current token.
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
        """parse consumes all of the tokens found in self.text looking for a
        set of expected tokens. Currently supported token sets are

        INTEGER PLUS INTEGER
        """
        # Just take whatever the first token is.
        self.current_token = self._next_token()

        # We expect that the first token was an integer.
        left = self.current_token
        self._consume_token(INTEGER)

        # The next expected Token is a PLUS
        OP = self.current_token
        self._consume_token(PLUS)

        # Lastly we expect another integer for addition to work.
        right = self.current_token
        self._consume_token(INTEGER)

        # Lastly we expect to run out of input.
        self._consume_token(EOF)

        # Since we now have INTEGER PLUS INTEGER we can add both integer
        # values together.
        result = left.value + right.value
        return result
