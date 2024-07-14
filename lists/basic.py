# It is a built in data type similar to String 
# it is mutable means that the indexed value of a list can be modified which is not possible in case of the string 
# It is different from arrays in other programming languages which is it can store any type of data (int, float, string, etc)
# syntax is listname=[listvalue1, listvalue2, ...]

marks=[38, 83, 37, 47, 57, 44]
print(marks)

mixedList=["adarsh", 83, 383.8, "shiva"]
print(mixedList)

# accessing and modifying list value from their index
print(marks[0])
marks[0]='fail'
print(marks)

# slicing: same as in string, accessing a small portion of list mean sublisting of a list.

print(marks[2:4])
