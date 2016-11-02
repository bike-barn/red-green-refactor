"""
All unit tests which focus on parsing of integers.
"""
import pytest

import calc


def test_calc_can_parse_single_digits():
    """
    Test that ``Calc.parse()`` can correctly parse single-digit integers.
    """
    assert False  # Don't just make this True.


def test_calc_can_parse_multiple_digits():
    """
    Test that ``Calc.parse()`` can correctly parse multi-digit integers.
    """
    assert False  # Don't just make this True.


def test_next_token_can_read_full_integers():
    """
    Test that ``Calc._next_token`` tokenizes an entire INTEGER token.

    Note:
        This test was added to help identify a bug where the expected
        :class:`Token` after an integer wasn't being correctly tokenized.
    """
    assert False  # Don't just make this True.
