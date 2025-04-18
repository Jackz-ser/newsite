import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Add a test user (optional)
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))

conn.commit()
conn.close()
print("Database initialized successfully.")
