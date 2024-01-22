""" 
 Create an inner function to calculate the addition in the following way:
- Create an outer function that will accept two parameters a and b
- Create an inner function inside an outer function that will calculate the
  addition of a and b
- At last, an outer function will add 5 into addition and return it
Date:22/12/23
""" 

# Outer function that adds two numbers and then adds 5 to the result
def outer_add(a, b):
    # Inner function that performs the actual addition
    def inner_add(a, b):
        return a + b

    # Call the inner function to get the sum of a and b
    result = inner_add(a, b)

    # Add 5 to the result obtained from the inner function
    return result + 5

# Example usage: Call outer_add with arguments 2 and 3
print(outer_add(2, 3))
 