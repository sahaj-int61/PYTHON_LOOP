"""
Create a function which returns compressed string of the data entered by the user.
Date:22/12/23
"""
def compress(string):
    compressed = ""
    count = 1

    # Iterate through the characters in the input string
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            # Increment the count if the current character is the same as the previous one
            count += 1
        else:
            # Append the character and its count to the compressed string
            compressed += string[i - 1] + str(count)
            count = 1

    # Append the last character and its count to the compressed string
    compressed += string[-1] + str(count)

    return compressed

# Get input from the user
user_input = input("Enter a string to compress: ")

# Call the compress function and display the result
result = compress(user_input)
print("Compressed string:", result)

'''
1. Function Definition:

   def compress(string):

   This line defines a function named `compress` that takes a string as its input. This function will perform the RLE compression on the input string.

2. Initialization:

   compressed = ""
   count = 1
   
   These lines initialize two variables:
   - `compressed`: This variable will store the compressed string.
   - `count`: This variable will keep track of the number of consecutive repetitions of a character.

3. Loop Through the String:

   for i in range(1, len(string)):
   
   This `for` loop iterates through each character in the input string, starting from the second character (index 1) and going up to the last character (index `len(string) - 1`).

4. Check for Consecutive Repetitions:

   if string[i] == string[i - 1]:
       count += 1
   
   Inside the loop, this `if` statement checks if the current character (`string[i]`) is the same as the previous character (`string[i - 1]`). If they are the same, it means we have found a consecutive repetition, so we increment the `count` variable.

5. Append Compressed Characters:

   else:
       compressed += string[i - 1] + str(count)
       count = 1
   
   If the current character is different from the previous character, it means we have reached the end of a consecutive repetition. In this case, we append the previous character and its count to the `compressed` string. We also reset the `count` variable to 1 for the next character.

6. Handle the Last Character:

   compressed += string[-1] + str(count)

   After the loop finishes, we need to handle the last character
'''