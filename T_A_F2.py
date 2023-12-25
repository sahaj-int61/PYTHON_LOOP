"""
Write a function func1() such that it can accept a variable length of arguments and print all argument's value.
Date: 21/12/23
""" 
def func1(*args):
    for arg in args:
        print(arg)

# Example usage:
func1(1, 2, 3) # Output: 1, 2, 3
func1("Hello", "World") # Output: Hello, World