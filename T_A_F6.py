"""
Create a function which generates a Python list of all the even numbers
between 0 to N.
Date:22/12/23
"""

# Function to generate a list of even numbers up to n
def generate_even_numbers(n):
    even_numbers = []  # Initialize an empty list to store even numbers
    for i in range(0, n + 1, 2):
        # Iterate through even numbers from 0 to n (inclusive) with a step of 2
        even_numbers.append(i)  # Add the current even number to the list
    return even_numbers  # Return the list of even numbers

# Example usage: Generate a list of even numbers up to 10
n = int(input("Enter the string: "))
even_numbers = generate_even_numbers(n)

# Print the list of even numbers
print(even_numbers)