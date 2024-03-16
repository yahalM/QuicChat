import binascii
import json
import re

import bcrypt

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return binascii.hexlify(hashed).decode()  # Convert bytes to hex string for storage

def check_password(user, password):
    stored_password = binascii.unhexlify(user.password.encode())
    return bcrypt.checkpw(password.encode(), stored_password)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hash_password(password)

    def is_valid(self):
        # Email regex pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        if not re.match(email_pattern, self.email):
            print("Email is invalid")
            return False, "Invalid user email format, please enter user@something.something"
        if check_password(self, ""):  # Simple check for non-empty password
            print("password is empty --> Invalid")
            return False, "Invalid user password, please enter non empty password"
        if not self.name:  # Simple check for non-empty password
            print("name is empty  --> Invalid")
            return False, "Invalid user name, please enter non empty user name"

        print("Valid user!")
        return True, ""

    def to_dict(self):
        # Return a copy of __dict__ excluding 'password' or any bytes type attribute
        return {k: v for k, v in self.__dict__.items() if not isinstance(v, bytes)}

    def __str__(self):
        user = {"User": self.to_dict()}
        return json.dumps(user)


# Example usage:
user1 = User("John Doe", "john.doe@example.com", "password123")
print(user1)
user1.is_valid()

user2 = User("John Doe", "john.doe@example", "password123")
print(user2)
user2.is_valid()

user3 = User("John Doe", "john.doe@example.com", "")
print(user3)
user3.is_valid()


user4 = User("", "john.doe@example.com", "password")
print(user4)
user4.is_valid()
