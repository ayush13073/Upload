import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hospital.db")

def get_connection():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def setup():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS hospital (
            hospital_id INTEGER PRIMARY KEY,
            hospital_name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT,
            established_year INTEGER
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doctor (
            doctor_Id INTEGER PRIMARY KEY,
            Name TEXT,
            specialization TEXT,
            phone TEXT,
            email TEXT,
            experience INTEGER,
            salary REAL,
            hospital_id INTEGER,
            FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id)
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

# ---------- INSERT ----------
def insert_hospital():
    v = (int(input("Hospital ID: ")), input("Hospital name: "),
         input("Address: "), input("City: "),
         int(input("Established year: ")))
    print(execute("INSERT INTO hospital VALUES (?,?,?,?,?)", v))

def insert_doctor():
    v = (int(input("Doctor ID: ")), input("Doctor name: "),
         input("Specialization: "), input("Phone: "), input("Email: "),
         int(input("Experience (years): ")), float(input("Salary: ")),
         int(input("Hospital ID: ")))
    print(execute("INSERT INTO doctor VALUES (?,?,?,?,?,?,?,?)", v))

# ---------- READ ----------
def view_hospitals():
    for r in execute("SELECT * FROM hospital", fetch=True): print(r)

def view_doctors():
    for r in execute("SELECT * FROM doctor", fetch=True): print(r)

def read_doctor_and_hospital(h, d):
    return execute("""
        SELECT h.hospital_name, h.address, h.city, h.established_year,
               d.Name, d.specialization, d.phone, d.email, d.experience, d.salary
        FROM hospital h JOIN doctor d ON h.hospital_id = d.hospital_id
        WHERE h.hospital_name = ? AND d.Name = ?
    """, (h, d), fetch=True)

def get_specialist_doctors_list(spec, salary):
    return execute("SELECT * FROM doctor WHERE specialization=? AND salary>?",
                   (spec, salary), fetch=True)

def get_doctors_by_hospital(h):
    return execute("""
        SELECT d.* FROM doctor d
        JOIN hospital h ON d.hospital_id = h.hospital_id
        WHERE h.hospital_name = ?
    """, (h,), fetch=True)

# ---------- UPDATE ----------
def update_doctor_experience(did, exp):
    return execute("UPDATE doctor SET experience=? WHERE doctor_Id=?", (exp, did))

def menu():
    setup()
    while True:
        print("""
--- Hospital Management (SQLite) ---
1. Insert Hospital
2. Insert Doctor
3. View Hospitals
4. View Doctors
5. Search Doctor & Hospital
6. Specialist Doctors by Salary
7. Doctors by Hospital
8. Update Doctor Experience
9. Exit
""")
        ch = input("Enter choice: ").strip()
        try:
            if   ch == '1': insert_hospital()
            elif ch == '2': insert_doctor()
            elif ch == '3': view_hospitals()
            elif ch == '4': view_doctors()
            elif ch == '5':
                rows = read_doctor_and_hospital(input("Hospital name: "),
                                                input("Doctor name: "))
                if not rows: print("No match (check names / hospital_id link).")
                for r in rows: print(r)
            elif ch == '6':
                rows = get_specialist_doctors_list(input("Specialization: "),
                                                   float(input("Minimum salary: ")))
                if not rows: print("No match.")
                for r in rows: print(r)
            elif ch == '7':
                rows = get_doctors_by_hospital(input("Hospital name: "))
                if not rows: print("No doctors found.")
                for r in rows: print(r)
            elif ch == '8':
                print(update_doctor_experience(int(input("Doctor ID: ")),
                                               int(input("New experience: "))))
            elif ch == '9': break
            else: print("Invalid choice.")
        except sqlite3.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter a valid number.")

if __name__ == "__main__":
    menu()