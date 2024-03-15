from tinydb import TinyDB, Query
import bcrypt


def check_password(email, password):
    user = get_user(email)
    if user:
        stored_password = user[0]['password']
        return bcrypt.checkpw(password.encode(), stored_password)
    return False


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


class UserDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.User = Query()

    def set_user(self, user):
        hashed_password = hash_password(user.password)
        user = {
            'nickname': user.nickname,
            'email': user.email,
            'password': hashed_password,  # Store the hashed password
            'picture': user.picture
        }
        return self.db.insert(user)

    def get_user(self, email):
        return self.db.search(self.User.email == email)
    def delete_user(self, email):
        self.db.remove(self.User.email == email)

    def update_user(self, email, **updates):
        if 'password' in updates:
            updates['password'] = hash_password(updates['password'])
        self.db.update(updates, self.User.email == email)

