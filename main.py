from employee import employee_menu
from salary import salary_menu
from department import department_menu
from attendance import attendance_menu
from reports import reports_menu

def main():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Employee Records")
        print("2. Salary")
        print("3. Department")
        print("4. Attendance")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            employee_menu()
        elif choice == "2":
            salary_menu()
        elif choice == "3":
            department_menu()
        elif choice == "4":
            attendance_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            print("Thank you.")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    main()
