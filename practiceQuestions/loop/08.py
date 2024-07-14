# Print numbers from 1 to 100
"""
i=1
while i<=100:
    print(i)
    i+=1
"""
# Print numbers from 100 to 1
"""
i=100
while i>=1:
    print(i)
    i-=1
"""

# Print the multiplication table of a number n
"""
n=int(input("n = "))
i=1
while i<=10:
    r=n*i
    print(r)
    i+=1
"""

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(num) :
    print(num[index])
    index += 1
"""

"""
i=1
list1=[]
while i<=10:
    list1.append(i**2)
    i+=1
print(list1)
"""
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

tuple2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(tuple2)
x = int(input("Enter number : "))
i = 0
while i<10:
    if(tuple2[i]==x):
        print("Number found at position : ",i+1)
    i+=1

"""
tuple1=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(tuple1)
x=int(input("x : "))
i = 1
check=0
while i<=10:
    temp = i**2
    if(temp==x):
        check=1
    i+=1
if(check==1):
    print("element found.")
else:
    print("Element not found.")
"""
