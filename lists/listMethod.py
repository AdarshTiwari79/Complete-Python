# list.append(value) -> to add a new element in the end of the existing list
rupees=[38, 83, 48, 34, 36]
rupees.append(47)
print(rupees)

# list.sort() -> To sort the existing list
rupees.sort()
print(rupees)

# list.sort(reverse=True) -> To sort the existing list in reverse order 
rupees.sort(reverse=True)
print(rupees)

# list.reverse() -> To reverse the existing list
rupees.reverse()
print(rupees)

# list.insert(index, element) -> insert an element at specific index
rupees.insert(3,"Adarsh")
print("after insert : ", rupees)

# list.remove(1) -> remove the first occurance of the element
list1=[3,5,8,3,8,6]
list1.remove(3)
print(list1)

# list.pop(index) -> remove element at the index
list1.pop(0)
print(list1)