"""
Use a loop to display elements from a given list which are present at even positions.
Date: 21/12/23
""" 

# A list of integers
my_list = [10 ,30 ,40 ,60 ,90 ,100 ,20 ,50] #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through the indices of the list
for i in range(len(my_list)):
    # Check if the index is odd (using i % 2 == 1)
    if i % 2 == 0:
        # Print the element at the odd index
        print(my_list[i])