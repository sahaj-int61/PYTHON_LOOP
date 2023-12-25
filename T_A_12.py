"""
Display Fibonacci series up to N terms.
Date: 21/12/23
"""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

N = 10
for i in range(N):
    print(fibonacci(i))