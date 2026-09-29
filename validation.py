def get_number(message, minimum=0):
    while True:
        try:
            n = int(input(message))
            if n < minimum:
                print("Enter a value of", minimum, "or more.")
            else:
                return n
        except ValueError:
            print("Please enter a number.")

def get_salary(message):
    while True:
        try:
            n = float(input(message))
            if n < 0:
                print("Salary cannot be negative.")
            else:
                return n
        except ValueError:
            print("Please enter a valid salary.")

def find_employee(employee_id, employees):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None
