import sqlite3, os, hashlib

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "customer.db")

def get_connection():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def setup():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerId INTEGER PRIMARY KEY,
            Name TEXT,
            Address TEXT,
            contact TEXT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit(); cur.close(); conn.close()

def hash_password(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200000)
    return salt.hex() + ":" + digest.hex()

def execute(sql, values=(), fetch=False):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, values)
    if fetch:
        rows = cur.fetchall()
        cur.close(); conn.close()
        return rows
    conn.commit()
    cur.close(); conn.close()
    return "Operation successful."

def insert_customer():
    v = (int(input("Customer ID: ")), input("Name: "), input("Address: "),
         input("Contact: "), input("Username: "),
         hash_password(input("Password: ")))
    print(execute("INSERT INTO Customer VALUES (?,?,?,?,?,?)", v))

def view_customers():
    for r in execute("SELECT CustomerId, Name, Address, contact, username FROM Customer",
                     fetch=True):
        print(r)

def search_customer():
    cid = int(input("Customer ID: "))
    rows = execute("""SELECT CustomerId, Name, Address, contact, username
                      FROM Customer WHERE CustomerId=?""", (cid,), fetch=True)
    if not rows: print("No customer found.")
    for r in rows: print(r)

def update_customer():
    cid = int(input("Customer ID to update: "))
    v = (input("New name: "), input("New address: "),
         input("New contact: "), input("New username: "), cid)
    print(execute("""UPDATE Customer
                     SET Name=?, Address=?, contact=?, username=?
                     WHERE CustomerId=?""", v))

def update_password():
    cid = int(input("Customer ID: "))
    print(execute("UPDATE Customer SET password=? WHERE CustomerId=?",
                  (hash_password(input("New password: ")), cid)))

def delete_customer():
    print(execute("DELETE FROM Customer WHERE CustomerId=?",
                  (int(input("Customer ID to delete: ")),)))

def menu():
    setup()
    while True:
        print("""
--- Customer Management (SQLite) ---
1. Insert Customer
2. View All Customers
3. Search Customer by ID
4. Update Customer Details
5. Update Password
6. Delete Customer
7. Exit
""")
        ch = input("Enter choice: ").strip()
        try:
            if   ch == '1': insert_customer()
            elif ch == '2': view_customers()
            elif ch == '3': search_customer()
            elif ch == '4': update_customer()
            elif ch == '5': update_password()
            elif ch == '6': delete_customer()
            elif ch == '7': break
            else: print("Invalid choice.")
        except sqlite3.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter valid input.")

if __name__ == "__main__":
    menu()