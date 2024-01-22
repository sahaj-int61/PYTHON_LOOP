"""
Print the following patter using the loop.
Date: 21/12/23
"""
# Initialize the number of rows
n = int(input("Enter number of rows to print: "))

# Outer loop iterates over each row
for i in range(n, 0, -1):
    print(i)
    # Inner loop iterates over each column in the current row
    for j in range(i, 0, -1):
        # Print the current number followed by a space
        print(j, end=" ")
    # Print a newline after each row
    print()