# WAP to input 2 int numbers, a and b
# Print True if a is greater than or equal to b. If not print False.

num1=int(input("Enter first integer number: "))
num2=int(input("Enter second integer number: "))

result=("True") if(num1>=num2) else ("False") #using ternary operator
print("using ternary operator ",result)

r2=("False","True")[num1>=num2] #using claver if
print("Using claver if ",r2)

if(num1>=num2):
    print("True")
else:
    print("False")
    