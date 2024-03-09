import sqlite3
import json


class SimpleDB:
    def __init__(self, db_name='simple_db.sqlite'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_document(self, document):
        data_json = json.dumps(document)
        query = 'INSERT INTO documents (data) VALUES (?)'
        self.conn.execute(query, (data_json,))
        self.conn.commit()

    def get_all_documents(self):
        query = 'SELECT data FROM documents'
        cursor = self.conn.execute(query)
        documents = [json.loads(row[0]) for row in cursor.fetchall()]
        return documents

    def close_connection(self):
        self.conn.close()

# Example usage:
db = SimpleDB()
all_documents = db.get_all_documents()
if len(all_documents) != 2:
    # Insert a document
    document1 = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    db.insert_document(document1)

    # Insert another document
    document2 = {'name': 'Jane Smith', 'age': 25, 'city': 'San Francisco'}
    db.insert_document(document2)

# Retrieve all documents
all_documents = db.get_all_documents()
print("All Documents:", all_documents)

# Close the database connection
db.close_connection()
