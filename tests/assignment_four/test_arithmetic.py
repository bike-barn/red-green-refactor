"""
All unit tests which focus on parsing of operators.
"""
import pytest

import calc


def test_calc_can_parse_subtraction():
    """
    Test that ``Calc.parse()`` can correctly parse subtraction.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiplication_by_one():
    """
    Test that ``Calc.parse()`` can correctly parse multiplication by one.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiplication_of_positive_integers():
    """
    Test that ``Calc.parse()`` can correctly parse multiplication of two
    positive integers.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_addition_of_zero():
    """
    Test that ``Calc.parse()`` can correctly parse adding zero to an integer.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_subtraction_of_zero():
    """
    Test that ``Calc.parse()`` can correctly parse subtracting zero from an
    integer.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_division_by_one():
    """
    Test that ``Calc.parse()`` can correctly parse a divisive identity.
    """
    assert False  # Don't just make this True.


def test_calc_parses_integer_division_instead_of_floating_point_division():
    """
    Test that ``Calc.parse()`` does integer division rather than floating point
    division. That is to say, parsing an expression that has a fractional
    remainder should yield a truncated result.

    Note:
        Yes, this is an obscenely long function name.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_division_of_zero():
    """
    Test that ``Calc.parse()`` can correctly parse division by zero.
    """
    assert False  # Don't just make this True.


def test_calc_raises_zero_division_error():
    """
    Test that ``Calc.parse()`` raises a ``ZeroDivision`` error when
    parsing would invole division by zero.

    Rabbit hole:
        You may have seen ``pytest.raises`` in some of the other tests. In
        Python the

        >>> with some_callable():
        ...     # do something

        syntax identifies what's known as a context manager.

        What a context manager is or does is a topic for another time, but in
        this case we are using it to "trap" the ``ZeroDivision`` error raised by
        ``Calc.parse()`` and then continue as if nothing had happened. If
        ``Calc.parse()`` does not raise a ``ZeroDivision`` error then pytest
        raises its own error and the test fails.

        If you'd like know more about context managers here's a great blog post!
        https://jeffknupp.com/blog/2016/03/07/python-with-context-managers
    """
    input_text = "10/0"
    calculator = calc.Calc(text=input_text)
    with pytest.raises(ZeroDivisionError):
        calculator.parse()

    # Oh, hey, look. We did this one for you. Have a giant rabbit hole instead!
    # When you're done just remove the line below this comment and that's it.
    assert False
