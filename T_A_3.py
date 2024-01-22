"""
Accept number from user and calculate the sum of all number between 1 and given number.
Date: 21/12/23
"""

# Ask the user to input a number
num = int(input("Enter a number: "))

# Initialize variable 'sum' to store the sum of numbers
sum = 0

# Use a for loop to iterate over each number from 1 to given number
for i in range(1, num + 1):
    # Add the current number to the sum
    sum += i

# Print the sum of all numbers between 1 and given number
print(sum)