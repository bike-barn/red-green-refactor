# NOTE: So when I made this I made the mistake of switching the token strings.
# My "test_eof_at_end_of_line" test found the error.
INTEGER, EOF, PLUS = 'INTEGER', 'EOF', 'PLUS'

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
