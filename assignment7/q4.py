import pyodbc
import hashlib
import os

SERVER   = "MSCCS44-HP"
USERNAME = "sa"
PASSWORD = "sql2025"
DRIVER   = "{ODBC Driver 18 for SQL Server}"

def get_connection(database="master", autocommit=False):
    conn_str = (
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        f"DATABASE={database};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str, autocommit=autocommit)

def connect_db():
    return get_connection("CustomerManagement", autocommit=False)

def setup():
    conn = get_connection("master", autocommit=True)
    cur = conn.cursor()
    cur.execute("IF DB_ID('CustomerManagement') IS NULL CREATE DATABASE CustomerManagement")
    cur.close(); conn.close()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        IF OBJECT_ID('Customer','U') IS NULL
        CREATE TABLE Customer (
            CustomerId INT PRIMARY KEY,
            Name VARCHAR(255),
            Address VARCHAR(255),
            contact VARCHAR(20),
            username VARCHAR(100) UNIQUE,
            password VARCHAR(256)
        )
    """)
    conn.commit()
    cur.close(); conn.close()

def hash_password(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200000)
    return salt.hex() + ":" + digest.hex()

def execute(sql, values=(), fetch=False):
    conn = connect_db()
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
    for r in execute("""SELECT CustomerId, Name, Address, contact, username
                        FROM Customer""", fetch=True):
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
--- Customer Management ---
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
        except pyodbc.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter valid input.")

if __name__ == "__main__":
    menu()