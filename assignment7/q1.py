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
    return get_connection("HospitalManagement", autocommit=False)

def setup():
    # CREATE DATABASE must be autocommit
    conn = get_connection("master", autocommit=True)
    cur = conn.cursor()
    cur.execute("IF DB_ID('HospitalManagement') IS NULL CREATE DATABASE HospitalManagement")
    cur.close(); conn.close()

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        IF OBJECT_ID('hospital','U') IS NULL
        CREATE TABLE hospital (
            hospital_id INT PRIMARY KEY,
            hospital_name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            city VARCHAR(100),
            established_year INT
        )
    """)
    cur.execute("""
        IF OBJECT_ID('doctor','U') IS NULL
        CREATE TABLE doctor (
            doctor_Id INT PRIMARY KEY,
            Name VARCHAR(255),
            specialization VARCHAR(100),
            phone VARCHAR(15),
            email VARCHAR(100),
            experience INT NULL,
            salary DECIMAL(10,2),
            hospital_id INT,
            FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id)
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

# ---------- INSERT ----------
def insert_hospital():
    v = (int(input("Hospital ID: ")),
         input("Hospital name: "),
         input("Address: "),
         input("City: "),
         int(input("Established year: ")))
    print(execute("INSERT INTO hospital VALUES (?,?,?,?,?)", v))

def insert_doctor():
    v = (int(input("Doctor ID: ")),
         input("Doctor name: "),
         input("Specialization: "),
         input("Phone: "),
         input("Email: "),
         int(input("Experience (years): ")),
         float(input("Salary: ")),
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
        FROM hospital h
        JOIN doctor d ON h.hospital_id = d.hospital_id
        WHERE h.hospital_name = ? AND d.Name = ?
    """, (h, d), fetch=True)

def get_specialist_doctors_list(spec, salary):
    return execute(
        "SELECT * FROM doctor WHERE specialization=? AND salary>?",
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
--- Hospital Management ---
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
                rows = read_doctor_and_hospital(input("Hospital name: "), input("Doctor name: "))
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
        except pyodbc.Error as e: print("DB error:", e)
        except ValueError:         print("Please enter a valid number.")

if __name__ == "__main__":
    menu()