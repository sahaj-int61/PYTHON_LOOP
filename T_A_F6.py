"""
Create a function which generates a Python list of all the even numbers
between 0 to N.
Date:22/12/23
"""

def generate_even_numbers(n):
    even_numbers = []
    for i in range(0, n + 1, 2):
        even_numbers.append(i)
    return even_numbers
even_numbers = generate_even_numbers(10)
print(even_numbers)