"""

NOTE: There are no tests that check for data validation at this point since
the interpreter doesn't have any data validation as a feature.
"""
import pytest

import pascal_interpreter as augur

def test_no_defaults():
    # There's no valid defaults at the moment.
    with pytest.raises(TypeError):
        augur.Token()

def test_known_type():
    # There's no valid defaults at the moment.
    token = augur.Token(type=augur.INTEGER, value=2)
    assert token.value == 2
    assert token.type == augur.INTEGER

def test_str_non_string_value():
    token = augur.Token(type=augur.INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert token.__str__() == expected_result

def test_repr():
    token = augur.Token(type=augur.INTEGER, value=2)
    expected_result = "Token(type=INTEGER, value=2)"
    assert token.__repr__() == expected_result
