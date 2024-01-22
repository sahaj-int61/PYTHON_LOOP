"""
Reverse the following list using for loop
Date: 21/12/23
"""
# Initial list of integers
list = [10, 20, 30, 40, 50]

# Create an empty list
l = [] 

# Iterate through each element in the original list
for i in list:
    # Use the `insert()` method to insert the element at the beginning of the new list
    l.insert(0, i)

# Print the reversed list
print(l)