# set.add(element) ->  adds an element 

set1=set()
set1.add('Adarsh')
set1.add('Ravana')
set1.add('Tiwari')
set1.add('Saurav Tiwari')
set1.add('Gopu')
set1.add('Sumit')
print(set1)

# set.remove(element) -> removes the element 

set1.remove('Gopu')
print(set1)

# set.pop() -> removes a random value
set1.pop()
print(set1)

# set.clear() -> empties the set or delete all elements of the set
set1.clear()
print(set1)

# set.union(set2) -> combines both set values and return the new set

marks1={33,32, 44, 53, 52, 54}
marks2={33,53,88, 89,76,6}
result=marks1.union(marks2)
print(result)
print(type(result))


# set.intersection(set2) -> combines common values & returns new
result2=marks2.intersection(marks1)
print(result2)