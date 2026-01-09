import random
import string

def generate_password(length: int = 20):
    if length < 4 or length > 128:
        raise ValueError("Password length must be between 4 and 128")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password
