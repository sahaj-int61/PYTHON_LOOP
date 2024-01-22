"""
Create a function which returns a given list:
Date:22/12/23
example:
input: [[1,2,3], [4,5,6], [7,8,9]]
output: [[1,4,7], [2,5,8], [3,6,9]
"""

# Function to create a new list by rearranging elements from sublists in a random sequence
def random_sequence(input_list):
    output_list = []  # Initialize an empty list to store the rearranged elements
    for i in range(len(input_list[0])):
        sub_list = []  # Initialize an empty sublist for each iteration
        for sub in input_list:
            sub_list.append(sub[i])  # Append the ith element from each sublist to the current sublist
        output_list.append(sub_list)  # Append the current sublist to the output list
    return output_list  # Return the final rearranged list

# Example usage: Create a new list by rearranging elements from the input list
input_list = [[1,2,3], [4,5,6], [7,8,9]] 
input_list1 = [["A", "B", "C"], ["P", "Q", "R"], ["X", "Y", "Z"]]
output_list = random_sequence(input_list)
output_list1 = random_sequence(input_list1)
# Print the rearranged list
print(output_list)
print(output_list1)