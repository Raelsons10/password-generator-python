from generator import generator_password
import string
def test_valid_generator_password_length():
    val = 12
    assert len(generator_password(val)) == val

def test_validate_password_generator_characters():
    val = 12
    password = generator_password(val)

    has_number = any(carac.isdigit() for carac in password)
    has_uppercase = any(carac.isupper() for carac in password)
    haas_lowercase = any(carac.islower() for carac in password)
    has_symbol = any(carac in string.punctuation for carac in password)
    assert has_number
    assert has_uppercase
    assert haas_lowercase
    assert has_symbol

