"""
All unit tests which focus on how whitespace is handled by the calculator.

Note:
    Some of these tests may seem redudant and that a single function to handle
    all whitespace possibilities in one ``assert`` might be enough. In this case
    you're probably right, but sometimes it can be useful to write verbose tests
    that consider pre, mid, and post conditions. They might help you pinpoint
    exactly how something is failing.

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


def test_calc_can_parse_whitespace_correctly():
    """
    Test that ``Calc.parse()`` can handle whitespace correctly.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_pre_whitespace_correctly():
    """
    Test that ``Calc.parse()`` handles whitespace at the start of input text.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_post_whitespace_correctly():
    """
    Test that ``Calc.parse()`` handles whitespace at the end of input text.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_mid_whitespace_correctly():
    """
    Test that ``Calc.parse()`` handles whitespace in the middle of input text.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_all_forms_of_whitespace():
    """
    Test that ``Calc.parse()`` can handle other forms of whitespace besides just
    the space character. What other forms of whitespace exist?
    """
    assert False  # Don't just make this True.
