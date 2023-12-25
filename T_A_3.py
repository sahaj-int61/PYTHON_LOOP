"""
Accept number from user and calculate the sum of all number between 1 and given number.
Date: 21/12/23
"""

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)