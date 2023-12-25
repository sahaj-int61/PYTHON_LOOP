"""
python program to display all the prime numbers within a range. 
Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers.
Date: 21/12/23
"""

start = 25
end = 50
  
print ("The Prime Numbers between 25 to 50 is:  ")  
for number in range (start, end + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)