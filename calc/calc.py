"""This program is an interpreter for a subset of the PASCAL programming
language. It's' based off of the Let's Build A Simple Interpreter tutorial
found at https://ruslanspivak.com/lsbasi-part1/

This code base was build and tested in Python3.5.
"""
# NOTE: So when I made this I made the mistake of switching the token strings.
# My "test_eof_at_end_of_line" test found the error.
INTEGER, EOF, PLUS = 'INTEGER', 'EOF', 'PLUS'

class InterpreterError(Exception):
    """Default exception for the interpter. Only thrown as a last resort. 
    Normally this means a more strict exception wasn't found. If you see this
    kind of exception in the wild consider putting in an enchancement request
    for a more narrow exception type for the given erroneous input.
    """
    pass

class Token:

    def __init__(self, type, value):
        """Simple creation method used to build Tokens.

        args:
            type: A name used to associate what kind and parameters of data
                that will be present in the Token object.
            value: A value that's hopefully valid for the passed in data type.
                example is that INTEGER type is associated with 
                -1, 0, 1, 2, ...

        NOTE: no verification of data is currently being done. Later versions
        of this class should check for invalid values based on passed in type
        and invalide types.
        """
        self.type = type
        self.value = value

    def __str__(self):
        """Produces a human readable representation of this objects meta data
        and data.

        For now this is simple enough that we're just returning the machine
        readable format. Subject to change as complexity increases.
        """
        return self.__repr__()

    def __repr__(self):
        """Produces a string that, if passed to a python interpreter with the
        Token type defined, will create a new Token object with the current
        variables.
        """
        return "Token(type={type}, value={value})".format(
                type=self.type,
                value=self.value,
            )

class Interpreter:

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

    def _error(self) -> None:
        """
        """
        # NOTE: force students to test these kinds of functions so they catch
        # things like mis-namings.
        raise InterpreterError()

    def _next_token(self) -> Token:
        """This is the method that calls the token class and breaks the input
        text into a set of tokens. This set of operations is called lexical
        analyization.
        """
        text = self.text
        position = self.position

        # Check to make sure we haven't run out of characters. If we have,
        # return an EOF token.
        if position > len(text) - 1:
            # NOTE: forgot the return statement and test caughtn it.
            return Token(EOF, None)

        # Get the character that's at the current position.
        current_character = text[position]

        if current_character.isdigit():
            self.position += 1
            return Token(INTEGER, int(current_character))

        if current_character == "+":
            self.position += 1
            return Token(PLUS, current_character)

        # if this method is called then an error will be raised.
        self._error()

    def _consume_token(self, token_type):
        """consume_token checks the current tokens type with the token type
        that's passed in. If they don't match then an error is raised.

        args:
            token_type: You can think of the token_type as the token that is
                next expected and should be found.
        """
        if self.current_token.type == token_type:
            self.current_token = self._next_token()
        else:
            # Mistake: Accidently named this function self.error()
            self._error()

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


def main():
    while True:
        try:
            text = input("calc>")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.parse()
        print(result)

if __name__ == "__main__":
    main()
