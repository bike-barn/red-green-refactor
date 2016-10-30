"""All Unit tests which focus on how whitespace is handled by the calculator.

Rabbit Hole:
    If you wanted to write the tests in this module in a more compact way and
    keep all of the same functionality here's how you could do it. This
    requires explaining decorators, parametrization, how test reporting works,
    and iterators. We chose to go with the more verbose but simpler
    implementation below.

@pytest.mark.parametrize('input_text', [
    ' 1 + 1 ',
    ' 1+1',
    '1+1 ',
    '1 + 1',
    ' 1\t+\f\v 1\n',
])
def test_whitespace(input_text):
    calc = Calc(text=input_text)
    assert calc.parse() == 2
"""
import pytest

from calc import INTEGER, EOF, PLUS, Calc, CalcError


def test_parse_handles_whitespace_correctly():
    input_text = " 1 + 1 "
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_handles_pre_whitespace_correctly():
    # These tests are redundant in that the first should handle this case but
    # sometimes it's useful for clarifications reasons to include tests like
    # this to pinpoint if pre, post, or mid conditions are failing and in what
    # combination.
    input_text = " 1+1"
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_handles_post_whitespace_correctly():
    input_text = "1+1 "
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_handles_mid_condition_whitespace_correctly():
    input_text = "1 + 1"
    calc = Calc(text=input_text)
    assert calc.parse() == 2


def test_parse_handles_all_forms_of_whitespace():
    input_text = " 1\t+\f\v 1\n"
    calc = Calc(text=input_text)
    assert calc.parse() == 2
