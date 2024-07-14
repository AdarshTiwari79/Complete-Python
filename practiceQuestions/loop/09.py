# using for 
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in num:
    print(el)
"""

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(num)
x = int(input("Enter number : "))
check = 0
for ele in num:
    if(ele==x):
        check = 1
        break
if(check==1):
    print("number found")
else: 
    print("not found")
