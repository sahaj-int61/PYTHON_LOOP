"""
Print the following patter using the loop.
Date: 21/12/23
"""
rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()