"""
Reverse a given integer number.
Date: 21/12/23
""" 
number = 76542  
reverse_number = 0  

while (number > 0):  
    remainder = number % 10  
    reverse_number = (reverse_number * 10) + remainder  
    number = number // 10 
  
print(reverse_number) 