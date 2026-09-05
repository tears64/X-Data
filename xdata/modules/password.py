import secrets
import string

def generate(length=20):
    length = max(8, min(int(length), 256))
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}:,.?"
    return {
        "type": "password",
        "length": length,
        "password": "".join(secrets.choice(alphabet) for _ in range(length)),
    }
