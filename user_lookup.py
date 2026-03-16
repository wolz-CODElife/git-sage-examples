import sqlite3

def find_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    print("Executing:", query)
    cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    user_input = input("Enter username: ")
    results = find_user(user_input)
    print("Results:", results)
