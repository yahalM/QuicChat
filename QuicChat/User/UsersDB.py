from tinydb import TinyDB, Query

import User


class UserDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.User = Query()

    def set_user(self, user):
        user = {
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        return self.db.insert(user)

    def get_user(self, email):
        return self.db.search(self.User.email == email)

    def delete_user(self, email):
        self.db.remove(self.User.email == email)

    def update_user(self, email, **updates):
        self.db.update(updates, self.User.email == email)


# Example usage:
db = UserDB('users_example.json')
user1 = User.User("John Doe", "john.doe@example.com", "password123")
print(user1)
print("let's get it!")
print(db.get_user(user1.email))
print("let's set it!")
print(db.set_user(user1))
print("let's get it!")
print(db.get_user(user1.email))
print("let's delete it!")
print(db.delete_user(user1.email))
print("let's get it!")
print(db.get_user(user1.email))
