import pytest

from calc import INTEGER, EOF, PLUS, Calc, CalcError


def test_calc_blank_expression():
    """This test just makes sure :class:`Interpreter` can be instantiated."""
    input_text = ""
    Calc(text=input_text)


def test_calc_error_type():
    input_text = ""
    calc = Calc(text=input_text)
    with pytest.raises(CalcError):
        calc._error()


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
    # Mistake: Since _next_token changes the state of position you can't just
    # calc.current_token = calc.Token(INTEGER, 1)
    # You have to call _next_token.
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
    # NOTE: I misnamed this test function. Another function had the same name
    # For a little while and as such this test was never ran.
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
