"""
Create a function that can accept two arguments employee name and ID and
print its value as shown in the example, and if the ID is missing in function call
it should show it as 001:
Date: 21/12/23
""" 

def print_employee_details(employee_name, employee_id):
    if len(str(employee_id)) > 3:
        print("The employee ID does not exist.")
    else:
        print("Employee Name:", employee_name)
        print("Employee ID:", employee_id)

employee_name = input("Enter employee name: ")
employee_id = int(input("Enter employee ID: "))

print_employee_details(employee_name, employee_id)