"""
Create a function that can accept two arguments employee name and ID and
print its value as shown in the example, and if the ID is missing in function call
it should show it as 001:
Date: 21/12/23
""" 

# Function to print employee details based on name and ID
def print_employee_details(employee_name, employee_id="001"):
    # if len(employee_id)>3:
    #     employee_id = "001"
    # # if int(employee_id) > 999:
    # #     print("The employee ID does not exist.\nEmployee ID: 001")
    # # else:
    # Print employee details if the ID is valid
    print("Employee Name:", employee_name)
    print("Employee ID:", employee_id)

# Take user input for employee name and ID
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

# Call the function to print employee details
print("\nResult with missing ID in function call:")
print_employee_details(employee_name)
print("\nResult with ID in function call:")
print_employee_details(employee_name,employee_id)