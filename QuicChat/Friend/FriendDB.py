from tinydb import TinyDB, Query

# Assuming the Friend class is defined elsewhere, similar to the User class.
import Friend

class FriendDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.Friend = Query()

    def set_friend(self, friend):
        friend_dict = {
            'name': friend.name,
            'address': friend.address
        }
        return self.db.insert(friend_dict)

    def get_friend(self, name):
        return self.db.search(self.Friend.name == name)

    def delete_friend(self, name):
        self.db.remove(self.Friend.name == name)

    def update_friend(self, name, **updates):
        self.db.update(updates, self.Friend.name == name)

# Example usage:
db_path = 'friends_example.json'
friend_db = FriendDB(db_path)

# Assuming a Friend instance is created like this:
friend1 = Friend.Friend("Alice", "123 Wonderland Ave")
print(friend1)

print("Let's set it!")
print(friend_db.set_friend(friend1))

print("Let's get it!")
print(friend_db.get_friend(friend1.name))

print("Let's delete it!")
print(friend_db.delete_friend(friend1.name))

print("Let's get it again!")
print(friend_db.get_friend(friend1.name))
