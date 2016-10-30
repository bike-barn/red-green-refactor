"""
"""
import pytest

import calc


def test_parse_subtraction():
    input_text = "5-3"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 2


def test_parse_multiplication_identity():
    input_text = "1*1"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_multiplication_both_positive():
    input_text = "10*2"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 20


def test_parse_division_identity():
    input_text = "1/1"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_division_integer_division():
    input_text = "10/3"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 3


def test_parse_division_of_zero():
    input_text = "0/10"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 0


def test_parse_division_of_by_zero():
    input_text = "10/0"
    calculator = calc.Calc(text=input_text)
    with pytest.raises(ZeroDivisionError):
        calculator.parse()


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
