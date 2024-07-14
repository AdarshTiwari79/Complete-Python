# function: Block of statements that perform a specific task.

# Syntax : der func_name(param1, param2,..): ----> function definition
#                 return val 

# func_name(arg1, arg2,..) -------> function call
"""
def add(num1,num2):
    return (num1 + num2)
n1 = int(input("Enter num1 : "))
n2 = int(input("Enter num2 : "))
result = add(n1,n2)
print("The addition of these two numbers is : ",result)
"""
# avarage of three numbers 
"""
def avg(n1, n2, n3):
    return (n1+n2+n3)/3

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

average = avg(num1, num2, num3)

print("The average of above no. is : ",average)
"""
# Default parameter: these are used in case when no argument is pass to the function whill calling the function

def multiplication(a=2,b=3): # a and b have difault value of 2 and 3 respectively
    print(a*b)
    return a*b

multiplication() # calling function without passing arguments