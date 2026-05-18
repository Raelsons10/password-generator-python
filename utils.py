def is_an_integer(password):
    try:
        int(password)
        return True
    except ValueError:
        return False
    
def is_valid_password_length(password):
    return password >= 12