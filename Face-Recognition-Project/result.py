import sqlite3
import os

# Create database directory if it doesn't exist
db_dir = os.path.dirname(os.path.abspath(__file__)) + '/database'
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Connect to SQLite database (will create it if it doesn't exist)
conn = sqlite3.connect(db_dir + '/face_recognition.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Teacher TEXT,
    Email TEXT,
    Phone TEXT
)
''')
conn.commit()

# Example query - replace 'id' with actual ID value when using this code
id_to_find = id  # Assuming 'id' variable is defined elsewhere

# Query the database
cursor.execute('SELECT Name, Department FROM User WHERE id = ?', (id_to_find,))
result = cursor.fetchone()

if result:
    name, department = result
    print(name)
    print(department)
else:
    name = None
    department = None
    print("User not found")

# Close the connection
conn.close()