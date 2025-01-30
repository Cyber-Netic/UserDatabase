import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")
conn.commit()

# Function to add a user
def add_user(name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("User added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")

# Function to get all users
def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Function to delete a user by ID
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    print("User deleted successfully!")

# Function to update user email
def update_user_email(user_id, new_email):
    try:
        cursor.execute("UPDATE users SET email=? WHERE id=?", (new_email, user_id))
        conn.commit()
        print("User email updated successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")

# Sample Execution
if __name__ == "__main__":
    print("1. Adding Users...")
    add_user("Alice Johnson", "alice@example.com")
    add_user("Bob Smith", "bob@example.com")

    print("\n2. Fetching Users...")
    users = get_users()
    for user in users:
        print(user)

    print("\n3. Updating Bob's Email...")
    update_user_email(2, "bob.new@example.com")

    print("\n4. Deleting Alice...")
    delete_user(1)

    print("\n5. Fetching Users After Updates...")
    users = get_users()
    for user in users:
        print(user)

# Close the connection
conn.close()
