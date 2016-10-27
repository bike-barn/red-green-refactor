import pytest

from calc import INTEGER, EOF, PLUS, Calc, CalcError


def test_calc_can_be_instantiated_with_blank_expression():
    """
    Test that an :class:`Calc` can be instantiated with a blank
    expression.
    """
    input_text = ""
    Calc(text=input_text)


def test_calc_raises_error_on_invalid_tokens():
    """
    Test that invalid tokens cause a ``CalcError`` and that the exception stack
    trace contains useful information.
    """
    input_text = "lumberjack"  # Now with 100% more Monty Python references.
    calc = Calc(text=input_text)
    with pytest.raises(CalcError) as err:
        calc.parse()
    assert "Invalid token at position 0" in str(err.value)


def test_calc_raises_error_on_unexepected_syntax():
    """
    Test that unexpected syntax causes a ``CalcError`` and that the exception
    stack trace contains useful information.
    """
    input_text = "+"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError) as err:
        calc.parse()
    assert "Expected INTEGER at position 1, found PLUS" in str(err.value)


def test_calc_finds_eof_token_at_end_of_line():
    """
    Test that, upon finding an end of line, a :class:`Calc` correctly tokenizes
    an EOF :class:`Token`.
    """
    input_text = ""
    calc = Calc(text=input_text)
    assert calc._next_token().type == EOF


def test_calc_finds_eof_token_after_int():
    """
    Test that after consuming a solitary an INTEGER :class:`Token` a
    :class:`Calc` will correctly tokenize an EOF :class:`Token`.
    """
    input_text = "1"
    calc = Calc(text=input_text)
    token = calc._next_token()
    assert token.type == INTEGER
    assert token.value == 1
    assert calc._next_token().type == EOF


def test_calc_can_consume_valid_token():
    """Test that a :class:`Calc` can consume a valid :class:`Token`."""
    input_text = "1+1"
    calc = Calc(text=input_text)
    # Note: Since _next_token advances position one cannot simply
    # >>> calc.current_token = Token(INTEGER, 1)
    # The _next_token method MUST be called or this test will fail.
    calc.current_token = calc._next_token()
    calc._consume_token(INTEGER)
    assert calc.current_token.type == PLUS


def test_parse_supports_addition():
    """Test that a :class:`Calc` can correctly parse the addition operation."""
    # Note: This function name was briefly duplicated and therefore didn't run.
    input_text = "1+1"
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_sets_eof():
    """
    Test that successfully parsing an arithmetic expression sets the
    ``current_token`` attribute of a :class:`Calc` to EOF.
    """
    input_text = "1+1"
    calc = Calc(text=input_text)
    calc.parse()
    assert calc.current_token.type == EOF


def test_parse_raises_error_on_invalid_expression():
    """
    Test that attempting to parse an invalid expression allows a ``CalcError``
    to propagate correctly.
    """
    input_text = "+1"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError):
        calc.parse()
