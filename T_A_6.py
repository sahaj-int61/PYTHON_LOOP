"""
Given a number count the total number of digits in a number
Date: 21/12/23
"""
def count_digits(number):
    if number == 0:
        return 1
    if number < 0:
        number = -number
    digits = 0
    while number > 0:
        number //= 10
        digits += 1
    return digits

number = int(input("Enter a number: "))
total_digits = count_digits(number)
print(f"The number is: {number} ,So the output is: {total_digits}.")