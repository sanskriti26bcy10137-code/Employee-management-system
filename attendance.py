from data import employees
from validation import get_number, find_employee

def attendance_menu():
    while True:
        print("\n--- Attendance ---")
        print("1. Record attendance")
        print("2. View attendance")
        print("3. Attendance report")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            record_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            attendance_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def record_attendance():
    employee = find_employee(get_number("Enter employee ID: ", 1), employees)
    if employee is None:
        print("Employee not found.")
        return

    total = get_number("Enter total working days: ", 1)
    present = get_number("Enter days present: ", 0)

    if present > total:
        print("Present days cannot be more than working days.")
        return

    employee["total_days"] = total
    employee["present"] = present
    print("Attendance saved.")

def attendance_percentage(employee):
    if employee["total_days"] == 0:
        return 0
    return employee["present"] / employee["total_days"] * 100

def view_attendance():
    employee = find_employee(get_number("Enter employee ID: ", 1), employees)
    if employee is None:
        print("Employee not found.")
        return

    print("Name:", employee["name"])
    print("Present:", employee["present"])
    print("Working days:", employee["total_days"])
    print("Attendance:", round(attendance_percentage(employee), 2), "%")

def attendance_report():
    for employee in employees:
        print(employee["id"], employee["name"], "-",
              round(attendance_percentage(employee), 2), "%")
