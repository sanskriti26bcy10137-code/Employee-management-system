from data import employees
from attendance import attendance_percentage

def reports_menu():
    while True:
        print("\n--- Reports ---")
        print("1. Total employees")
        print("2. Highest salary")
        print("3. Department count")
        print("4. Average attendance")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Total employees:", len(employees))
        elif choice == "2":
            highest_salary()
        elif choice == "3":
            department_report()
        elif choice == "4":
            attendance_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def highest_salary():
    if len(employees) == 0:
        print("No employee records.")
        return

    highest = employees[0]
    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    print("Highest salary employee:", highest["name"])
    print("Salary:", highest["salary"])

def department_report():
    counts = {}

    for employee in employees:
        department = employee["department"]
        if department in counts:
            counts[department] = counts[department] + 1
        else:
            counts[department] = 1

    for department in counts:
        print(department, ":", counts[department])

def attendance_summary():
    if len(employees) == 0:
        print("No employee records.")
        return

    total = 0
    for employee in employees:
        total = total + attendance_percentage(employee)

    print("Average attendance:", round(total / len(employees), 2), "%")
