a=3
b=1.53
integerDivision=a//b
print(integerDivision,a/b)
print(type(integerDivision),type(a/b))

num1=-3.5
num2=1.5
result=num1//num2
print(result)
print(type(result))

# so the difference between normal division and integer division is that in normal division directly conversion of result into float
# while in integer division(//) firstly float converted into integer like 0.33 into 0, 0.99 into 0 and then convert them into float
# floor is same used to get closest integer same as integer division