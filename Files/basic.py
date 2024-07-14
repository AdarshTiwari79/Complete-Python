# there are two types of files : 1. text files---> .txt, .docs, .log
# 2. binary files----> .mov, .png, .jpeg etc.
# these two type are surface level classification of files at the end all files are stored in the form of bits in the computer


# Open, Read & close File

# We have to open a file before reading or writing.
# syntax: f=open("file_name","mode")----> here file_name should be sample.txt, demo.docs etc. and mode should be r : read mode, w : write mode
# data = f.read()
# f.close()

# Different mode symbols:
"""
'r' : open for reading (default)
'w' : open for writing, truncating the file first.
'x' : create a new file and open it for writing 
'a' : open for writing, appending to the end of the file if it exists
'b' : binary mode
't' : text mode (default)
'+' : open a disk file for updating (reading and writing)
"""
"""
r+ : read and overwrite (pointer at start) and no truncate
w+ : read and overwrite truncate
a+ : read and append (pointer at end) and no truncate
"""
"""
f = open("abc.txt",'x')
f.write("This file is created through python file I/O commands.")
f.close()
"""

f = open("abc.txt",'r')
print(f.read())
f.close()