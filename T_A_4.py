"""
Print multiplication table of given number.
Date: 21/12/23
"""
# Request the number to multiply from the user
print("Enter the number to multiply: ")
num = int(input())

# Start a loop to iterate from 1 to 10 (inclusive)
for i in range(1, 11):
    #print(i, end="")
    # Multiply the number entered by the user with the current iteration number
    print(num * i)