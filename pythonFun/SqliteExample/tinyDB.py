from tinydb import TinyDB, Query

# Create a TinyDB instance and create a table (collection)
db = TinyDB('my_database.json')

# Insert a document
db.insert({'name': 'John', 'age': 25, 'city': 'Example'})

# Query the database
User = Query()
result = db.search(User.name == 'John')
print(result)

# Update a document
db.update({'age': 26}, User.name == 'John')
# Insert a document
User = Query()
result = db.search(User.name == 'Doe')
if len(result) == 0:
    db.insert({'name': 'Doe', 'age': 34, 'city': 'ExampleCity'})
# Remove a document
db.remove(User.name == 'John')

# Close the database connection
db.close()
