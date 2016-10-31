"""
Tests focused on proving the calculator can accept any number of arguments
"""
import pytest

import calc


def test_parse_multiple_addition_operations():
    input_text = "1 + 2 + 3 + 4"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 10


def test_parse_multiple_subtraction_operations():
    input_text = "0 - 2 - 3 - 4"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == -9


def test_parse_combined_addition_and_subtraction():
    input_text = "0 + 2 - 3 + 4"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 3


def test_parse_combined_with_division():
    input_text = "0 + 3 / 3 + 4"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 5


def test_parse_combined_with_multiplication():
    input_text = "0 + 6 / 3 * 2"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 4


def test_parse_multiple_division_operations():
    input_text = "6 / 3 / 2"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_multiple_multiplication_operations():
    input_text = "2 * 3 * 2"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 12


def test_double_operators_throw_exception():
    input_text = "2 *2 ** 2"
    calculator = calc.Calc(text=input_text)
    with pytest.raises(calc.CalcError) as error:
        calculator.parse()
        expected_message = "'DIVIDED_BY'] at position 7, found INTEGER"
        assert str(error.value) == expected_message


def test_double_integers_throw_exception():
    input_text = "2 * 2 2 * 2"
    calculator = calc.Calc(text=input_text)
    with pytest.raises(calc.CalcError) as error:
        calculator.parse()
        expected_message = (
            "calc.calc.CalcError: Expected ['PLUS', 'MINUS', 'TIMES',"
            "'DIVIDED_BY'] at position 7, found INTEGER")
        assert str(error.value) == expected_message
