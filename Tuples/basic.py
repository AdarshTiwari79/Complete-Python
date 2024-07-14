# same as string and list.
# tuples are immutable in nature means that the elements of a tuple can not be modified.
# syntax of tuples -> tupleName = (elements)
# tuple having only one element is defined as tupleName = (e,). If we donot use comma then it will be treated as normal type element as integer or float or string

tup=()
print(type(tup))

tup1=(3) # treated as integer 
print(type(tup1))

tup2=(3,8,0)
print(tup2)

# accessing element of the tuple
print(tup2[2])

# slicing is same as in string and lists
print(tup2[1:])

