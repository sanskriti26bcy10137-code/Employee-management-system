from data import employees

def department_menu():
    while True:
        print("\n--- Department ---")
        print("1. Show departments")
        print("2. Employees in a department")
        print("3. Department count")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            show_departments()
        elif choice == "2":
            show_by_department()
        elif choice == "3":
            department_count()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def show_departments():
    departments = set()
    for employee in employees:
        departments.add(employee["department"])

    print("\nDepartments:")
    for department in departments:
        print(department)

def show_by_department():
    name = input("Enter department: ")
    found = False

    for employee in employees:
        if employee["department"].lower() == name.lower():
            print(employee["id"], "-", employee["name"])
            found = True

    if not found:
        print("No employee found.")

def department_count():
    counts = {}

    for employee in employees:
        department = employee["department"]
        if department in counts:
            counts[department] = counts[department] + 1
        else:
            counts[department] = 1

    for department in counts:
        print(department, ":", counts[department])
