"""
 Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration.
Date: 21/12/23
"""
string = input("Enter a list of numbers separated by spaces: ") #[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

number_strings = string.split()

list = [int(num) for num in number_strings]
for i in list:
    # Break the loop if the current number is greater than 150
    if i > 150:
        break

    # If the current number is divisible by 5, print it
    if i % 5 == 0:
        print(i, end=",")
        