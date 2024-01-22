"""
Create a function which returns the largest and smallest number from the
given list.
Date:22/12/23
"""

def func(numbers):
    # Check if the list is not empty
    if not numbers:
        return None, None  # Return None for both largest and smallest if the list is empty

    # Initialize variables for the largest and smallest numbers
    largest = smallest = numbers[0]

    # Iterate through the list to find the largest and smallest numbers
    for num in numbers:
        if num > largest:
            # print(largest)
            print(num)
            largest = num
        if num < smallest:
            # print(smallest)
            # print(num)
            smallest = num

    return largest, smallest

numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_num, smallest_num = func(numbers_list)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)

'''
1. Function Definition

def func(numbers):

The `func` function is defined with one parameter, `numbers`, which is expected to be a list containing numeric values.

2. Checking for Empty List

    # Check if the list is not empty
    if not numbers:
        return None, None  # Return None for both largest and smallest if the list is empty

Before proceeding, the function checks if the input list `numbers` is empty. If the list is empty, it returns `None` for both the largest and smallest numbers. This is done to handle the case where there are no numbers in the list.

3. Initialization of Variables

    # Initialize variables for the largest and smallest numbers
    largest = smallest = numbers[0]

The function initializes two variables, `largest` and `smallest`, both set to the first element of the input list `numbers`. This is done to ensure that the initial values for comparison are set.

4. Iterating Through the List

    # Iterate through the list to find the largest and smallest numbers
    for num in numbers:

The code enters a `for` loop that iterates through each element (`num`) in the input list `numbers`.

5. Comparison and Updating

        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

Inside the loop, there are two conditional statements:

- If the current number (`num`) is greater than the current largest number (`largest`), it updates the `largest` variable to the current number.
- If the current number (`num`) is smaller than the current smallest number (`smallest`), it updates the `smallest` variable to the current number.

6. Returning the Result

    return largest, smallest

After iterating through the entire list, the function returns the `largest` and `smallest` numbers as a tuple.
'''