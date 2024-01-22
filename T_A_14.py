"""
Reverse a given integer number.
Date: 21/12/23
""" 
# Initialization of variables
number = 76542 
reverse_number = 0 

# Loop to reverse the number
while (number > 0): 
    # Extract the last digit from the number
    remainder = number % 10 

    # Append the last digit to the reversed number
    reverse_number = (reverse_number * 10) + remainder 

    # Remove the last digit from the number
    number = number // 10 

# Print the reversed number
print(reverse_number) 