"""
Write a function func1() such that it can accept a variable length of arguments and print all argument's value.
Date: 21/12/23
""" 
# Function to print the values of arbitrary arguments (*args)
def func1(*args):
    # Iterate through each argument in the args tuple
    for arg in args:
        print(arg)

# Example usage with integers
func1(1, 2, 3)

# Example usage with strings
func1("Hello", "World")

