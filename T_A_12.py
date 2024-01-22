"""
Display Fibonacci series up to N terms.
Date: 21/12/23
"""
# Function to calculate the nth Fibonacci number
def fibonacci(n):
    a, b = 0, 1  # Initialize the first two numbers in the Fibonacci sequence
    for _ in range(n):
        a, b = b, a + b  # Update values to generate the next Fibonacci number
    return a  # Return the nth Fibonacci number

N = 10  # Number of Fibonacci numbers to generate
for i in range(N):
    print(fibonacci(i))  # Print the ith Fibonacci number for each iteration