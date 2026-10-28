import pyodbc

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
    return get_connection("StudentManagement", autocommit=False)

def setup():
    conn = get_connection("master", autocommit=True)
    cur = conn.cursor()
    cur.execute("IF DB_ID('StudentManagement') IS NULL CREATE DATABASE StudentManagement")
    cur.close(); conn.close()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        IF OBJECT_ID('Student','U') IS NULL
        CREATE TABLE Student (
            StudentID INT PRIMARY KEY,
            name VARCHAR(255),
            date_of_birth DATE,
            contact_details VARCHAR(255),
            status VARCHAR(50)
        )
    """)
    conn.commit()
    cur.close(); conn.close()

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

def insert_student():
    v = (int(input("Student ID: ")), input("Name: "),
         input("Date of birth YYYY-MM-DD: "),
         input("Contact details: "), input("Status: "))
    print(execute("INSERT INTO Student VALUES (?,?,?,?,?)", v))

def view_students():
    for r in execute("SELECT * FROM Student", fetch=True): print(r)

def update_student():
    sid = int(input("Student ID to update: "))
    v = (input("New name: "), input("New DOB YYYY-MM-DD: "),
         input("New contact details: "), input("New status: "), sid)
    print(execute("""UPDATE Student
                     SET name=?, date_of_birth=?, contact_details=?, status=?
                     WHERE StudentID=?""", v))

def search_student():
    name = input("Enter student name: ")
    rows = execute("SELECT * FROM Student WHERE name LIKE ?",
                   ('%' + name + '%',), fetch=True)
    if not rows: print("No match.")
    for r in rows: print(r)

def delete_student():
    print(execute("DELETE FROM Student WHERE StudentID=?",
                  (int(input("Student ID to delete: ")),)))

def menu():
    setup()
    while True:
        print("""
--- Student Management ---
1. Insert Student
2. View All Students
3. Update Student
4. Search Student by Name
5. Delete Student
6. Exit
""")
        ch = input("Enter choice: ").strip()
        try:
            if   ch == '1': insert_student()
            elif ch == '2': view_students()
            elif ch == '3': update_student()
            elif ch == '4': search_student()
            elif ch == '5': delete_student()
            elif ch == '6': break
            else: print("Invalid choice.")
        except pyodbc.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter valid input.")

if __name__ == "__main__":
    menu()