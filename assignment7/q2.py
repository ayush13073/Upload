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
    return get_connection("LibraryManagement", autocommit=False)

def setup():
    conn = get_connection("master", autocommit=True)
    cur = conn.cursor()
    cur.execute("IF DB_ID('LibraryManagement') IS NULL CREATE DATABASE LibraryManagement")
    cur.close(); conn.close()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        IF OBJECT_ID('Member','U') IS NULL
        CREATE TABLE Member (
            MemberId INT PRIMARY KEY,
            MName VARCHAR(255),
            Email VARCHAR(255),
            Address VARCHAR(255),
            PhoneNo VARCHAR(20),
            MembershipDate DATE,
            ExpiryDate DATE
        )
    """)
    cur.execute("""
        IF OBJECT_ID('Book','U') IS NULL
        CREATE TABLE Book (
            BookId INT PRIMARY KEY,
            BookName VARCHAR(255),
            AuthorName VARCHAR(255),
            PublicationYear INT,
            Price DECIMAL(10,2)
        )
    """)
    cur.execute("""
        IF OBJECT_ID('[Transaction]','U') IS NULL
        CREATE TABLE [Transaction] (
            TransactionId INT PRIMARY KEY,
            BookId INT,
            MemberID INT,
            IssueDate DATE,
            DueDate DATE,
            ReturnDate DATE,
            FinalAmount DECIMAL(10,2),
            Status VARCHAR(50),
            FOREIGN KEY (BookId)   REFERENCES Book(BookId),
            FOREIGN KEY (MemberID) REFERENCES Member(MemberId)
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

# ---------- MEMBER ----------
def insert_member():
    v = (int(input("Member ID: ")), input("Name: "), input("Email: "),
         input("Address: "), input("Phone: "),
         input("Membership date YYYY-MM-DD: "), input("Expiry date YYYY-MM-DD: "))
    print(execute("INSERT INTO Member VALUES (?,?,?,?,?,?,?)", v))

def view_members():
    for r in execute("SELECT * FROM Member", fetch=True): print(r)

def update_member():
    mid = int(input("Member ID to update: "))
    v = (input("New name: "), input("New email: "), input("New address: "),
         input("New phone: "), input("Membership date YYYY-MM-DD: "),
         input("Expiry date YYYY-MM-DD: "), mid)
    print(execute("""UPDATE Member
                     SET MName=?, Email=?, Address=?, PhoneNo=?,
                         MembershipDate=?, ExpiryDate=?
                     WHERE MemberId=?""", v))

def delete_member():
    print(execute("DELETE FROM Member WHERE MemberId=?",
                  (int(input("Member ID to delete: ")),)))

# ---------- BOOK ----------
def insert_book():
    v = (int(input("Book ID: ")), input("Book name: "), input("Author name: "),
         int(input("Publication year: ")), float(input("Price: ")))
    print(execute("INSERT INTO Book VALUES (?,?,?,?,?)", v))

def view_books():
    for r in execute("SELECT * FROM Book", fetch=True): print(r)

def update_book():
    bid = int(input("Book ID to update: "))
    v = (input("New book name: "), input("New author: "),
         int(input("New year: ")), float(input("New price: ")), bid)
    print(execute("""UPDATE Book
                     SET BookName=?, AuthorName=?, PublicationYear=?, Price=?
                     WHERE BookId=?""", v))

def delete_book():
    print(execute("DELETE FROM Book WHERE BookId=?",
                  (int(input("Book ID to delete: ")),)))

# ---------- TRANSACTION ----------
def issue_book():
    v = (int(input("Transaction ID: ")), int(input("Book ID: ")),
         int(input("Member ID: ")), input("Issue date YYYY-MM-DD: "),
         input("Due date YYYY-MM-DD: "))
    print(execute("""
        INSERT INTO [Transaction]
        (TransactionId, BookId, MemberID, IssueDate, DueDate, ReturnDate, FinalAmount, Status)
        VALUES (?,?,?,?,?, NULL, 0, 'Issued')
    """, v))

def view_transactions():
    for r in execute("SELECT * FROM [Transaction]", fetch=True): print(r)

def return_book():
    tid = int(input("Transaction ID: "))
    rdate = input("Return date YYYY-MM-DD: ")
    amount = float(input("Final amount: "))
    print(execute("""
        UPDATE [Transaction]
        SET ReturnDate=?, FinalAmount=?, Status='Returned'
        WHERE TransactionId=?
    """, (rdate, amount, tid)))

def menu():
    setup()
    while True:
        print("""
--- Library Management ---
1.  Insert Member
2.  View Members
3.  Update Member
4.  Delete Member
5.  Insert Book
6.  View Books
7.  Update Book
8.  Delete Book
9.  Issue Book
10. View Transactions
11. Return Book
12. Exit
""")
        ch = input("Enter choice: ").strip()
        try:
            if   ch == '1':  insert_member()
            elif ch == '2':  view_members()
            elif ch == '3':  update_member()
            elif ch == '4':  delete_member()
            elif ch == '5':  insert_book()
            elif ch == '6':  view_books()
            elif ch == '7':  update_book()
            elif ch == '8':  delete_book()
            elif ch == '9':  issue_book()
            elif ch == '10': view_transactions()
            elif ch == '11': return_book()
            elif ch == '12': break
            else: print("Invalid choice.")
        except pyodbc.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter valid input.")

if __name__ == "__main__":
    menu()