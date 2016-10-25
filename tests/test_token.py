"""

NOTE: There are no tests that check for data validation at this point since
the interpreter doesn't have any data validation as a feature.
"""
import pytest

from calc import INTEGER, Token


def test_no_defaults():
    # There's no valid defaults at the moment.
    with pytest.raises(TypeError):
        Token()


def test_known_type():
    # There's no valid defaults at the moment.
    token = Token(type=INTEGER, value=2)
    assert token.value == 2
    assert token.type == INTEGER


def test_str_non_string_value():
    token = Token(type=INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert str(token) == expected_result


def test_repr():
    token = Token(type=INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert repr(token) == expected_result
