"""
Tests focused on proving the calculator can accept any number of arguments
"""
import pytest

import calc


def test_calc_can_parse_multiple_addition_operations():
    """
    Test that ``Calc.parse()`` can handle multiple consecutive addition
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiple_subtraction_operations():
    """
    Test that ``Calc.parse()`` can handle multiple consecutive subtraction
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_combined_addition_and_subtraction():
    """
    Test that ``Calc.parse()`` can handle combined addition and subtraction
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_division_with_other_operations():
    """
    Test that ``Calc.parse()`` can handle division combined with other
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiplication_with_other_operations():
    """
    Test that ``Calc.parse()`` can handle multiplication combined with other
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiple_division_operations():
    """
    Test that ``Calc.parse()`` can handle multiple consecutive division
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiple_multiplication_operations():
    """
    Test that ``Calc.parse()`` can handle multiple consecutive multiplication
    operations.
    """
    assert False  # Don't just make this True.


def test_calc_raises_error_when_parsing_adjacent_integers():
    """
    Test that ``Calc.parse()`` raises a ``CalcError`` if a given expression
    contains adjacent integers that are not part of a multi-digit integer. Test
    that the error message is correct.

    Rabbit hole:
        You may have seen the rabbit hole about context managers in assignnment
        four, but what's this ``as`` business? What does

        >>> with some_callable() as some_variable:
        ...     # do something with some_variable

        do? In this situation it allows us to save the exception that is raised
        by ``Calc.parse()``, but "trapped" by ``pytest.raises``. We can then
        check that ``error.value`` contains the appropriate error message after
        it has been raised even though we never caught the exception ourselves.
    """
    input_text = "2 * 2 2 * 2"
    calculator = calc.Calc(text=input_text)
    expected_message = (
        "Expected ['PLUS', 'MINUS', 'TIMES','DIVIDED_BY'] at position 7, "
        "found INTEGER")
    with pytest.raises(calc.CalcError) as error:
        calculator.parse()
    assert str(error.value) == expected_message
    # Oh, hey, look. We did this one for you. Have a giant rabbit hole instead!
    # When you're done just remove the line below this comment and that's it.
    assert False


def test_calc_raise_error_when_parsing_adjacent_operators():
    """
    Test that ``Calc.parse()`` raises a ``CalcError`` if a given expression
    contains adjacent operators. Test that the error message is correct.
    """
    assert False  # You're on your own for this one. See above for an example.
