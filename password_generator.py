import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate_password(self, length_lower=8, length_upper=2, length_digits=2, length_special=2):
        # Génération des parties du mot de passe
        password_chars = []
        password_chars.extend(random.choice(self.lowercase) for _ in range(length_lower))
        password_chars.extend(random.choice(self.uppercase) for _ in range(length_upper))
        password_chars.extend(random.choice(self.digits) for _ in range(length_digits))
        password_chars.extend(random.choice(self.special) for _ in range(length_special))
        
        # Mélange du mot de passe
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
