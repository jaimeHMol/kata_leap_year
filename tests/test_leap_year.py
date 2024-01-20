import pytest

from leap_year.leap_year import is_leap


def test_happy_path_leap_year():
    """ Test the happy path to determine if a number is a leap year."""
    expected_result = False
    result = is_leap(1990)
    assert expected_result == result


def test_wrong_types_on_leap_year():
    """ Test the happy path to determine if a number is a leap year."""
    inputs = [1.32, -2010, "two"]
    for input in inputs:
        with pytest.raises(ValueError):
            is_leap(input)

def test_corner_cases_leap_year():
    """ Test some corner cases to determine if a number is a leap year."""
    test_params = [(2000, True), (2400, True), (1800, False), (1900, False), (2100, False), (2200, False), (2300, False), (2500, False)]
    for test_param in test_params:
        result = is_leap(test_param[0]) 
        assert test_param[1] == result
