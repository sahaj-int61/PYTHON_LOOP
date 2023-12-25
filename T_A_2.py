"""
 Print the following pattern.
Date: 21/12/23
"""
n = 5
for i in range(0, n):
	n = 1
	for j in range(0, i+1):
		print(n, end=" ")
		n = n+1
	print()
