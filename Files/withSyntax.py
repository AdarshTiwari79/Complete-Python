# syntactical way to open and do operation in file 
# this way you do not require to close the file each time with keyword will close the file for us

with open("abc.txt",'r') as f:
    data = f.read()
    print(data)