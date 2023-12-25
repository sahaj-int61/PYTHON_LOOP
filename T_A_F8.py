"""
Create a function which returns compressed string of the data entered by the user.
Date:22/12/23
"""
import zlib

def compress_string(input_string):
    return zlib.compress(input_string.encode('utf-8'))

user_input = input("Enter some data: ")

compressed_data = compress_string(user_input)

print(f"Compressed Data: {compressed_data}")