""" 
Write a recursive function to calculate the sum of numbers from 0 to 10.
Date:22/12/23
""" 
def calculate_sum(n):
   # Base case: If n is less than or equal to 0, return 0
   if n <= 0:
       return 0
   else:
       print(n)
       # Recursive case: Return n plus the sum of integers from 0 to n-1
       return n + calculate_sum(n - 1)
   

# Call the function with n = 10
sum = calculate_sum(10)

# Print the result
print("The sum from 0 to 10 is: ", sum)
