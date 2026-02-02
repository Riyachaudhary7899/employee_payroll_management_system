# main.py
# Employee Payroll Management System

from database import connect_db, create_table

def add_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))

    net_salary = basic + allowance - deduction

    cursor.execute("""
        INSERT INTO employees
        VALUES (?, ?, ?, ?, ?, ?)
    """, (emp_id, name, basic, allowance, deduction, net_salary))

    conn.commit()
    conn.close()
    print("✅ Employee added successfully!")


def view_employees():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    print("\n--- Employee Records ---")
    for row in records:
        print(row)

    conn.close()


def search_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to search: "))
    cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
    record = cursor.fetchone()

    if record:
        print("Employee Found:", record)
    else:
        print("❌ Employee not found")

    conn.close()


def update_salary():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to update: "))
    basic = float(input("Enter New Basic Salary: "))
    allowance = float(input("Enter New Allowance: "))
    deduction = float(input("Enter New Deduction: "))

    net_salary = basic + allowance - deduction

    cursor.execute("""
        UPDATE employees
        SET basic_salary=?, allowance=?, deduction=?, net_salary=?
        WHERE emp_id=?
    """, (basic, allowance, deduction, net_salary, emp_id))

    conn.commit()
    conn.close()
    print("✅ Salary updated successfully!")


def delete_employee():
    conn = connect_db()
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))

    conn.commit()
    conn.close()
    print("🗑 Employee deleted successfully!")


def main():
    create_table()

    while True:
        print("\nEMPLOYEE PAYROLL MANAGEMENT SYSTEM")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_salary()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice!")

main()
