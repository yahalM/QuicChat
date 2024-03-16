import json


class Friend:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def is_valid(self):
        # Simple checks for non-empty name and address
        if not self.name:
            print("Name is empty --> Invalid")
            return False, "Invalid friend name, please enter a non-empty name."

        if not self.address:
            print("Address is empty --> Invalid")
            return False, "Invalid friend address, please enter a non-empty address."

        print("Valid friend!")
        return True, ""

    def to_dict(self):
        # Convert the Friend object attributes to a dictionary
        return {"name": self.name, "address": self.address}

    def __str__(self):
        friend_dict = {"Friend": self.to_dict()}
        return json.dumps(friend_dict, indent=4)


# Example usage:
friend1 = Friend("Alice", "123 Wonderland Ave")
print(friend1)
validity, message = friend1.is_valid()
print(message)

friend2 = Friend("", "456 Fantasy Rd")
print(friend2)
validity, message = friend2.is_valid()
print(message)

friend3 = Friend("Bob", "")
print(friend3)
validity, message = friend3.is_valid()
print(message)
