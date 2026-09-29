from data import employees
from validation import get_number, get_salary, find_employee

def salary_menu():
    while True:
        print("\n--- Salary ---")
        print("1. Add or update salary")
        print("2. View salary")
        print("3. Salary summary")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            update_salary()
        elif choice == "2":
            view_salary()
        elif choice == "3":
            salary_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def update_salary():
    employee = find_employee(get_number("Enter employee ID: ", 1), employees)
    if employee is None:
        print("Employee not found.")
        return
    employee["salary"] = get_salary("Enter monthly salary: ")
    print("Salary saved.")

def view_salary():
    employee = find_employee(get_number("Enter employee ID: ", 1), employees)
    if employee is None:
        print("Employee not found.")
        return
    print("Name:", employee["name"])
    print("Monthly salary:", employee["salary"])
    print("Yearly salary:", employee["salary"] * 12)

def salary_summary():
    if len(employees) == 0:
        print("No employee records.")
        return

    total = 0
    highest = employees[0]

    for employee in employees:
        total = total + employee["salary"]
        if employee["salary"] > highest["salary"]:
            highest = employee

    print("Total monthly salary:", total)
    print("Average monthly salary:", round(total / len(employees), 2))
    print("Highest salary:", highest["name"], "-", highest["salary"])
