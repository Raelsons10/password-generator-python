import string
import secrets

def generator_password(password_length):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    generated_password = []
 
    for i in range(password_length):
        generated_password.append(secrets.choice(caracteres))
    return "".join(generated_password)

