"""
All Unit tests which focus on arithmatic operations in the calculator.
"""
import pytest

import calc


def test_parse_single_digits():
    input_text = "1+1"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 2

def test_parse_multiple_digits():
    input_text = "100+1"
    calculator = calc.Calc(text=input_text)
    assert calculator.parse() == 101

def test_next_token_read_full_int():
    # This test was added to fix a bug where the Token after an integer wasn't
    # being correctly grabbed.

    # NOTE: Potentially we don't need to add this to the assignment unit tests?
    input_text = "12"
    calculator = calc.Calc(text=input_text)
    token = calculator._next_token()
    assert token.type == calc.INTEGER
    assert token.value == 12
    assert calculator._next_token().type == calc.EOF
