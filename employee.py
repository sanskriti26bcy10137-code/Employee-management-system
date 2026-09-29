from data import employees
from validation import get_number, find_employee

def employee_menu():
    while True:
        print("\n--- Employee Records ---")
        print("1. Add employee")
        print("2. Show employees")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            show_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def add_employee():
    employee_id = get_number("Enter employee ID: ", 1)
    if find_employee(employee_id, employees) is not None:
        print("This ID already exists.")
        return

    name = input("Enter name: ")
    age = get_number("Enter age: ", 18)
    department = input("Enter department: ")

    employee = {
        "id": employee_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": 0,
        "present": 0,
        "total_days": 0
    }
    employees.append(employee)
    print("Employee added.")

def show_employees():
    if len(employees) == 0:
        print("No employees found.")
        return

    print("\nID  Name  Age  Department  Salary")
    for employee in employees:
        print(employee["id"], employee["name"], employee["age"],
              employee["department"], employee["salary"])

def search_employee():
    employee_id = get_number("Enter employee ID: ", 1)
    employee = find_employee(employee_id, employees)

    if employee is None:
        print("Employee not found.")
    else:
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Age:", employee["age"])
        print("Department:", employee["department"])
        print("Salary:", employee["salary"])

def update_employee():
    employee_id = get_number("Enter employee ID: ", 1)
    employee = find_employee(employee_id, employees)

    if employee is None:
        print("Employee not found.")
        return

    name = input("New name (Enter to keep old): ")
    department = input("New department (Enter to keep old): ")

    if name != "":
        employee["name"] = name
    if department != "":
        employee["department"] = department

    print("Details updated.")

def delete_employee():
    employee_id = get_number("Enter employee ID: ", 1)
    employee = find_employee(employee_id, employees)

    if employee is None:
        print("Employee not found.")
    else:
        employees.remove(employee)
        print("Employee deleted.")
