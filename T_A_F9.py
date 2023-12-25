"""
Create a function which returns a given list:
Date:22/12/23
example:
input: [[1,2,3], [4,5,6], [7,8,9]]
output: [[1,4,7], [2,5,8], [3,6,9]
"""

def random_sequence(input_list):
    output_list = []
    for i in range(len(input_list[0])):
        sub_list = []
        for sub in input_list:
            sub_list.append(sub[i])
        output_list.append(sub_list)
    return output_list

input_list = [["A","B","C"],["P","Q","R"],["X","Y","Z"]]
output_list = random_sequence(input_list)
print(output_list)