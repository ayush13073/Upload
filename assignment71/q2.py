import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.db")

def get_connection():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def setup():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Member (
            MemberId INTEGER PRIMARY KEY,
            MName TEXT, Email TEXT, Address TEXT, PhoneNo TEXT,
            MembershipDate TEXT, ExpiryDate TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Book (
            BookId INTEGER PRIMARY KEY,
            BookName TEXT, AuthorName TEXT,
            PublicationYear INTEGER, Price REAL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "Transaction" (
            TransactionId INTEGER PRIMARY KEY,
            BookId INTEGER, MemberID INTEGER,
            IssueDate TEXT, DueDate TEXT, ReturnDate TEXT,
            FinalAmount REAL, Status TEXT,
            FOREIGN KEY (BookId)   REFERENCES Book(BookId),
            FOREIGN KEY (MemberID) REFERENCES Member(MemberId)
        )
    """)
    conn.commit(); cur.close(); conn.close()

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
        INSERT INTO "Transaction"
        (TransactionId, BookId, MemberID, IssueDate, DueDate, ReturnDate, FinalAmount, Status)
        VALUES (?,?,?,?,?, NULL, 0, 'Issued')
    """, v))

def view_transactions():
    for r in execute('SELECT * FROM "Transaction"', fetch=True): print(r)

def return_book():
    tid = int(input("Transaction ID: "))
    rdate = input("Return date YYYY-MM-DD: ")
    amount = float(input("Final amount: "))
    print(execute("""
        UPDATE "Transaction"
        SET ReturnDate=?, FinalAmount=?, Status='Returned'
        WHERE TransactionId=?
    """, (rdate, amount, tid)))

def menu():
    setup()
    while True:
        print("""
--- Library Management (SQLite) ---
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
        except sqlite3.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter valid input.")

if __name__ == "__main__":
    menu()