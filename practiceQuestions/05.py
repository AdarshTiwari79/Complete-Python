# WAP to check if a number entered by the user is odd or even

number=int(input("Enter the number you want to check for even of odd : "))
if(number%2==0):
    print("it is an even number.")
else:
    print("it is an odd number.")

# wAP to find the greatest of 3 numbers entered by the user.

num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
num3=float(input("Enter third number : "))
if(num1>=num2 and num1>=num3):
    print("The greatest of all number is first : ",num1)
elif(num2>=num3):
    print("The greatest of all numbers is second : ",num2)
else:
    print("The greatest of all numbers is third : ",num3)

# WAP to check if a number is a multiple of 7 or not

num=int(input("Enter number : "))
if(num%7==0):
    print("Entered number is multiple of 7.")
else:
    print("Entered number is not multiple of 7.")
