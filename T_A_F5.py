""" 
Write a recursive function to calculate the sum of numbers from 0 to 10.
Date:22/12/23
""" 

def calculate_sum(n):
   if n <= 0:
       return 0
   else:
       return n + calculate_sum(n - 1)

sum = calculate_sum(10)
print("The sum from 0 to 10 is: ", sum)