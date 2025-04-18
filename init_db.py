import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Create the users table
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a test user
c.execute('''
    INSERT INTO users (username, password)
    VALUES (?, ?)
''', ("admin", "admin"))

conn.commit()
conn.close()

print("Database created with test user.")
