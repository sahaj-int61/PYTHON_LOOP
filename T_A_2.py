"""
 Print the following pattern.
Date: 21/12/23
"""
# This variable defines the size of the pattern
n = int(input("Enter a size: "))

# This loop iterates from 0 to n-1, inclusive
for i in range(0, n):
    # print(i)
    # This variable is used to initialize the first number in the sequence
    n = 1

    # This loop iterates from 0 to i, inclusive
    for _ in range(0, i+1):
        # Print the current number and a space character
        print(n, end=" ")

        # Increment the current number
        n = n+1

    # Print a newline character to start a new line for the next iteration
    print()