# Write a recursion function to calculate the sum of first n natural numbers.
"""
def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)

n = int(input("Enter number : "))
r = sum(n)
print("the sum of first ",n," natural numbers is ",r)
"""
# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

def show(list1, idx):
    if(idx==len(list1)):
        return
    print(list1[idx])
    show(list1, idx+1)

fruits = ['banana','apple','mango','papaya','orange']

show(fruits,0)
