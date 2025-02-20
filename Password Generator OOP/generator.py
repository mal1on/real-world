"""Password Generator"""


import random


CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"


class PasswordGenerator:
    """Password Generator"""

    def __init__(self, length):
        self.password = ''.join(random.choice(CHARACTERS)
                                for _ in range(length))
        self.strength = self.check_password()

    def check_password(self):
        """Check password strength"""
        criteria = {
            'length': len(self.password) >= 8,
            'lowercase': any(char.islower() for char in self.password),
            'uppercase': any(char.isupper() for char in self.password),
            'digit': any(char.isdigit() for char in self.password),
            'special': any(char in "!@#$%^&*()" for char in self.password)
        }
        strength = sum(criteria.values())
        return strength


if __name__ == '__main__':

    new_pass = PasswordGenerator(9)
    print(f'Generated password: {new_pass.password}')
    print(f'Password strength: {new_pass.strength} (out of 5)')
