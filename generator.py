import string
import secrets

def generator_password(password_length):
    
    mandatory_capital_letter = secrets.choice(string.ascii_uppercase)
    mandatory_lowercase_letter = secrets.choice(string.ascii_lowercase)
    mandatory_symbol = secrets.choice(string.punctuation)
    mandatory_number = secrets.choice(string.digits)

    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    generated_password = []

    generated_password.extend([mandatory_capital_letter, mandatory_lowercase_letter, mandatory_number, mandatory_symbol])
 
    for i in range(password_length - 4):
        generated_password.append(secrets.choice(caracteres))

    security = secrets.SystemRandom()
    security.shuffle(generated_password)
    return "".join(generated_password)

