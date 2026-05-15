# Test file for behavior predictability.

from utils import is_an_integer, is_valid_password_length

# Unit tests of the function is_valid_password_length.
def test_is_valid_password_length():
    val1 = 8
    val2 = 29
    assert is_valid_password_length(val1)
    assert is_valid_password_length(val2)
def test_is_invalid_password_length():
    val1 = 7
    val2 = 0
    val3 = -1
    assert not is_valid_password_length(val1)
    assert not is_valid_password_length(val2) 
    assert not is_valid_password_length(val3)

# Unit test of the function is_an_integer.
def test_is_an_integer():
    val = "12"
    assert is_an_integer(val)
def test_is_not_an_integer():
    val1 = "abc"
    val2 = "12.5"
    val3 = ""
    assert not is_an_integer(val1)
    assert not is_an_integer(val2)
    assert not is_an_integer(val3)