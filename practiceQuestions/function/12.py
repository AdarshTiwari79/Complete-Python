# WAF to print the length of a list. (list is the parameter)
"""
def listLength(list1):
    return len(list1)

num = [3, 'adarsh', 88, 'suraj', 38]
length = listLength(num)
print(length)
"""

# WAF to print the elements of a list in a single line. (list is the parameter)
"""
def display (list2):
    for i in list2: 
        print(i,end=" ")
num = [3, 'adarsh', 88, 'suraj', 38]  
display(num)  
"""

# WAF to find the factorial of n. (n is the parameter)
"""
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input("Enter number : "))
r = factorial(n)
print("The factorial of the given number is : ",r)
"""

# WAF to convert USD to INR
def USDtoINR(USD):
    INR = USD * 83
    return INR

u = int(input("Enter value in $ : "))
r = USDtoINR(u)
print(r)
        