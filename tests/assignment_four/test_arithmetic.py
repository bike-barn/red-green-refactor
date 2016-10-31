"""Operator focused testing"""
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


def test_parse_addition_identity():
    input_text = "1 + 0"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_subtraction_identity():
    input_text = "1 - 0"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_division_identity():
    input_text = "1/1"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 1


def test_parse_integer_division_instead_of_floating_division():
    input_text = "10/3"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 3


def test_parse_division_of_zero():
    input_text = "0/10"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 0


def test_parse_division_by_zero():
    input_text = "10/0"
    calculator = calc.Calc(text=input_text)
    with pytest.raises(ZeroDivisionError):
        calculator.parse()
