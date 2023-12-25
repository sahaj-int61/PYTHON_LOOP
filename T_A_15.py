"""
Use a loop to display elements from a given list which are present at even positions.
Date: 21/12/23
""" 

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if i % 2 == 1: # Check if the index is even
        print(my_list[i])