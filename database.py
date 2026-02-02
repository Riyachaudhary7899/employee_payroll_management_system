# database.py
# Handles database connection and table creation

import sqlite3

def connect_db():
    return sqlite3.connect("payroll.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            basic_salary REAL,
            allowance REAL,
            deduction REAL,
            net_salary REAL
        )
    """)

    conn.commit()
    conn.close()
