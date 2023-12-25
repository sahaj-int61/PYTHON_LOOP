"""
Write a loop to find the factorial of any number.
Date: 21/12/23
"""
def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Example usage:
n = int(input("write a number: "))
print(factorial(n)) # Output: 120   


'''
N = 10
for i in range(N):
    print(fibonacci(i))'''