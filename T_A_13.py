"""
Write a loop to find the factorial of any number.
Date: 21/12/23
"""
# Function to calculate the factorial of a number
def factorial(num):
    factorial = 1  # Initialize the factorial variable to 1
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by each number from 1 to num
    return factorial  # Return the final factorial value

# Example usage:
n = int(input("write a number: "))  # Take user input for a number
print(factorial(n))  # Calculate and print the factorial of the input number
# Example Output: For input 5, the output will be 120 (5! = 5 * 4 * 3 * 2 * 1)
   
