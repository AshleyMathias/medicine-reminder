import sqlite3

def connect_db():
    return sqlite3.connect("reminders.db")

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            medicine_name TEXT,
            dosage TEXT,
            date TEXT,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_reminder(patient, medicine, dosage, date, time):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO reminders (patient_name, medicine_name, dosage, date, time)
        VALUES (?, ?, ?, ?, ?)
    ''', (patient, medicine, dosage, date, time))
    conn.commit()
    conn.close()
