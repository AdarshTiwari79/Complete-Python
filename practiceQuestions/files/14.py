# Create a new file "practice.txt" using python. Add the following data in it:
"""
Hi everyone 
we are learning file I/O
using Java.
I like programming in Java.
"""

"""
# import os
# os.remove('practic.txt')

with open("practic.txt",'x') as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing Java.\nI like programming in Java.")
    

with open("practic.txt",'r') as f:
    print(f.read())
"""

# WAF that replace all occurances of "java" with "python" in above file.
"""
with open("practic.txt",'r') as f:
    data = f.read()

new_data = data.replace("Java","Python")

with open("practic.txt",'w') as f:
    f.write(new_data)

with open("practic.txt",'r') as f:
    data = f.read()
    print(data)
"""

# Search if the world "learning" exists in the file or not.
"""
with open("practic.txt",'r') as f:
    data = f.read()

count = 0
count = data.find("learning")
if(count > 0):
    print("exists")
else: 
    print("not exists")
"""

# WAF to find in which line of the file does the word "learning" occur first.
# print -1 if the word not found.
"""
def check_for_line():
    data = True
    line_no = 1
    word = "learning"
    with open("practic.txt",'r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1


check_for_line()
"""

# From a file containing numbers separated by comma, print the count of even numbers.
# with open("number.txt","x") as f:
#     f.write("1,2,4,3,5,2,8,37,89,79")

with open("number.txt",'r') as f:
    data = f.read()

num = data.split(",")
print(num)
count = 0
for i in num:
    if(int(i)%2==0):
        count+=1
print(count)
"""
num = ''
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

"""
    



