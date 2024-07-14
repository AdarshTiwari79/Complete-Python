# Loops are used for sequencial traversal. For traversing list, string, tuples etc.
"""
list2=[3, "Adarsh", 33, "Shivam", 899]
for el in list2:
    print(el)
"""

list2=[3, "Adarsh", 33, "Shivam", 899]
for el in list2:
    if(el=="Adarsh"):
        print("element found")
        break
    print(el)
else: print("end loop") # print only when complete loop executes
