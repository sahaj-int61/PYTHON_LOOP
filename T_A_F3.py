""" 
Write a function calculation() such that it can accept two variables and
calculate the addition and subtraction of it. And also it must return both
addition and subtraction in a single return call.
Date:21/12/23
""" 
def calculation(x, y):
   addition = x + y
   subtraction = x - y
   return addition, subtraction
addition, subtraction = calculation(int(input("Enter a number x: ")),int(input("Enter a number y: ")))
print("Addition: ", addition)
print("Subtraction: ", subtraction)