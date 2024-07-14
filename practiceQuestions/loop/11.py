# WAP to find the sum of first n numbers.(using while loop)
"""
n = int(input("Enter number upto which you want to add : "))
i = 1
sum = 0
while i<=n:
    sum += i
    i+=1
print("Addition of first ",n," natural numbers is : ",sum)
"""
# WAP to find the factorial of first n natural numbers (using for)

n = int(input("Enter number : "))
factorial = 1
for i in range(1,n+1,1):
    factorial *= i
print("factorial of ",n," is : ",factorial)
