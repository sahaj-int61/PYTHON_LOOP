"""
Given a number count the total number of digits in a number
Date: 21/12/23
"""
def count_digits(number):
    if number == 0:
        # Special case: If the input is zero, the function returns 1 because a zero is a single digit.
        return 1
    # Using floor division (//) to get the quotient and modulus (%) to get the remainder.
    if number < 0:
        # If the input is negative, the function converts it to a positive number because the count of digits is the same for both positive and negative numbers.
        number = -number
        # Convert the positive value to negative so that we can handle negative numbers correctly.
    digits = 0
    while number > 0:
        # This loop keeps dividing the input number by 10 until it becomes zero.
        # The number of times the loop runs is the total number of digits in the input number.
        number //= 10
        print(number)
        digits += 1
        print(digits)
    return digits

print(count_digits(int(input("Enter number: "))))
