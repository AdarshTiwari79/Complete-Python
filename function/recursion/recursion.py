# Recursion  is when a fuction call itself
# Recursion is similar to a loop but sometime it is better to use recursion in loop
"""
def show(n):
    if(n==0): # base case: just like in loop condition are used to stop the loop. In similar manner base case are used to stop recursion
        return
    print(n)
    show(n-1)

show(8)
"""
# factorial calculation using recursion 

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter number : "))
r = fact(n)
print("Factorial of ",n," is ",r)
