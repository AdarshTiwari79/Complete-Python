"""
count = 1 # this variable is generally known as iterators
num=int(input("Enter number : "))
while count<=10:
    result=num*count
    count+=1
    print(result)
"""

# Reverse loop 
"""
i=10
num=int(input("enter number : "))
while i>=1:
    result=num*i
    i-=1
    print(result)
"""
# break: used to terminate the loop when encountered
"""
i = 1
while i<20:
    print(i)
    if(i==9):
        break
    i+=1
"""
# continue: terminates execution in the current iteration & continues execution of the loop with the next iteration.

i=1
while i<20:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
