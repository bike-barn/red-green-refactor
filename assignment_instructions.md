# Assignment One

## Running Assignment One Tests
For assignment one `pytest` should be invoked from the command line at the root
of the project directory like so
```bash
pytest tests/assignment_one/test_token.py
```

## Instructions

The goal for assignment one is to make the tests in `tests/test_token.py` pass.
When finished there should be a `Token` class in `calc/token.py` that can be
instantiated with a `type` and a `value`. Calling the `str()` built-in on a
newly instantiated `Token` should generate a string that, if copied and pasted
back into an interpreter, should yield the same `Token`.


```python
>>> from calc import Token
>>> token = Token(type=INTEGER, value=3)
>>> str(token)
'Token(type=INTEGER, value=3)'
>>> Token(type=INTEGER, value=3)
>>> # This means you have made a token successfully.
```


# Assignment Two

## Running Assignment Two Tests

For assignment two `pytest` should be invoked from the command line at the root
of the project directory like so
```bash
pytest tests/assignment_one/test_token.py tests/assignment_two/test_calc.py
```
If you're feeling particularly daring and your shell supports the syntax you
can try running it like this instead
```bash
pytest tests/assignment_{one,two}
```
## Instructions
**NOTE:** When you're finished with Assignment Two re-run Assignment One's
tests to make sure they still pass.

The goal for assignment two is to make the tests in `tests/test_calc.py` pass.
When finished there should be a `Calc` calss that can be instantiated with some
`text`. Calling `Calc.parse()` should produce a valid result given text like
`1+1` (`INTEGER PLUS INTEGER`).

Start with `calc/calc.py` and look at the `calc` classes `parse` method. The
control flow for this assigment is `parse` calls `_consume_token`, 
`_consume_token` calls `_next_token`.

```python
>>> from calc import Calc
>>> calc = Calc(text='1+1')
>>> calc.parse()
2
>>> # This means your calculator successfully parsed addition.
```

The only arithmetic operation that needs to be supported by your calculator at
this point is addition. Please note that the calculator cannot handle
whitespace currently. Don't fret, _you'll_ fix this in assignment three.

If the above is true then you should also be able to run your calculator
directly from the command line like
```bash
user@hostname:~/Projects/calc $ calc
calc> 1+1
2
calc> %
user@hostname:~/Projects/calc $
```

# Assignment Three

## Running Assignment Three Tests

For assignment two `pytest` should be invoked from the command line at the root
of the project directory like so
```bash
python -m pytest tests/assignment_three/test_consume_whitespace.py
python -m pytest tests/assignment_three/test_tokenize_integers.py
```

The shell completion syntax
```bash
pytest tests/assignment_{one,two,three}
```

## Instructions
In this assignment we're going to be adding two new functions who are going to
be in charge of tokenizing arbitrary sized integers and another function in
charge of ignoring whitespace.

### Tokinzing Integers
```python
def _tokenize_integer(self, text):
    """If have found a single digit then this helper function will read
    characters until the end of the integer is found.

    NOTE: This function is the one that will advance `self.position`.

    Args:
        text: A section of the text that is assumed to contain an integer

    Returns:
        Token

    Raises:
        None
    """
    pass
```

### Ignoring Whitespace

```python
def _consume_whitespace(self, text):
    """Eats all whitespace found until there's nothing left.

    NOTE: This function may advance `self.position`.

    Args:
        text: The input text to have whitespace removed until a non
                whitespace character is found.

    returns:
        None

    raises:
        None
    """
```

## Example Run
```bash
user@hostname:~/Projects/calc $ calc
calc> 22 + 2
24
calc> 4 +          4
16
calc> 10 + \t 4
14
```

# Assignment Four

## Running Assignment Four Tests

For assignment two `pytest` should be invoked from the command line at the root
of the project directory like so
```bash
python -m pytest tests/assignment_four/test_arithmetic.py
```

The Shell Completion
```bash
pytest tests/assignment_{one,two,three,four}
```

## Instructions

In this section you're going to add three new Tokens, `MINUS`, `TIMES`,
and `DIVIDED_BY`. After those tokens exist you'll have to modify `_next_token`
and `parse` such that these new operations are supported.

## Example Run

```bash
user@hostname:~/Projects/calc $ calc
calc> 2 / 2
0
calc> 4 - 2
2
calc> 10 * 4
40
```

### Assignment Five

## Running Assignment Five Tests

For assignment two `pytest` should be invoked from the command line at the root
of the project directory like so
```bash
python -m pytest tests/assignment_four/test_arbitrary_operators.py
```

The Shell Completion
```bash
pytest tests/assignment_{one,two,three,four,five}
```

## Instructions
The final assignment (unless you want to ask us about extra credit) will be
adding support for any number of operations. This means you'll need to add
code to `parse` that will look for a left integer, an operation, and a
right integer, complete the operation, and then look for a new right integer
until you run out of input.

Hint:
    The old right integer will become the new left integer.


**NOTE:** Order of operations aren't expected to be correct yet. That's much
more work. =P
## Example Run

```bash
user@hostname:~/Projects/calc $ calc
calc> 2 * 2 / 2
2
calc> 2 / 2 * 0
0
calc> 50 * 2 + 1
101
```
