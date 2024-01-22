"""
python program to display all the prime numbers within a range. 
Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers.
Date: 21/12/23
"""

# Get user input for the starting and ending numbers of the range
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
  
# Display a message indicating that prime numbers will be printed
print("The Prime Numbers between", start, "and", end, "are:")
  
# Iterate through the numbers in the specified range
for number in range(start, end + 1):
    # Check if the current number is greater than 1
    if number > 1:
        
        # Iterate from 2 to the current number to check for factors
        for i in range(2, number):
            print(number)
           
            # If the current number is divisible by any number in the range, it's not prime
            if (number % i) == 0:
                break
        else:
            # If no factors were found, the number is prime; print it
            print(number, end=",")