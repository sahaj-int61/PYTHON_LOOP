""" 
Write a function calculation() such that it can accept two variables and
calculate the addition and subtraction of it. And also it must return both
addition and subtraction in a single return call.
Date:21/12/23
""" 
# Function to perform addition and subtraction on two numbers
def calculation(x, y):
    # Calculate addition and subtraction
    addition = x + y
    subtraction = x - y
    # Return both results as a tuple
    return addition, subtraction

# Take user input for two numbers
x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

# Call the calculation function with user-provided values
addition, subtraction = calculation(x, y)

# Print the results
print("Addition:",addition, "Subtraction:",subtraction)
# print("Subtraction: ", subtraction)