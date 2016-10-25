import pytest

from calc import INTEGER, EOF, PLUS, Calc, CalcError


def test_calc_blank_expression():
    """This test just makes sure :class:`Interpreter` can be instantiated."""
    input_text = ""
    Calc(text=input_text)


def test_raises_error_on_invalid_tokens():
    """
    Test that invalid tokens cause a ``CalcError`` and that the exception stack
    traace contains useful information.
    """

    input_text = "foo"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError) as err:
        calc.parse()
    assert "Invalid token at position 0" in str(err.value)


def test_raises_error_on_unexepected_syntax():
    """
    Test that unexpected syntax causes a ``CalcError`` and that the exception
    stack trace contains useful information.
    """

    input_text = "+"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError) as err:
        calc.parse()
    assert "Expected INTEGER at position 1, found PLUS" in str(err.value)


def test_invalid_string_errors():
    input_text = "This is currently an error"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError):
        calc._next_token()


def test_eof_token_at_end_of_line():
    input_text = ""
    calc = Calc(text=input_text)
    assert calc._next_token().type == EOF


def test_eof_token_after_int():
    input_text = "1"
    calc = Calc(text=input_text)
    token = calc._next_token()
    assert token.type == INTEGER
    assert token.value == 1
    assert calc._next_token().type == EOF


def test_consume_valid_token():
    input_text = "1+1"
    calc = Calc(text=input_text)
    # Note: Since _next_token advances position one cannot simply
    # >>> calc.current_token = Token(INTEGER, 1)
    # The _next_token method MUST be called or this test will fail.
    calc.current_token = calc._next_token()
    calc._consume_token(INTEGER)
    assert calc.current_token.type == PLUS


def test_consume_invalid_token():
    input_text = "+1"
    calc = Calc(text=input_text)
    calc.current_token = calc._next_token()
    with pytest.raises(CalcError):
        calc._consume_token(INTEGER)


def test_parse_addition():
    # Note: This function name was briefly duplicated and therefore didn't run.
    input_text = "1+1"
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_sets_eof():
    input_text = "1+1"
    calc = Calc(text=input_text)
    calc.parse()
    assert calc.current_token.type == EOF


def test_parse_invalid_addition():
    input_text = "+1"
    calc = Calc(text=input_text)
    with pytest.raises(CalcError):
        calc.parse()
