""" 
 Create an inner function to calculate the addition in the following way:
- Create an outer function that will accept two parameters a and b
- Create an inner function inside an outer function that will calculate the
  addition of a and b
- At last, an outer function will add 5 into addition and return it
Date:22/12/23
""" 

def func_add(a, b):
    def inner_add(a, b):
        return a + b
    result = inner_add(a, b)
    return result + 5

print(func_add(2, 3)) 