# WAP to ask the user to enter names of their 3 favorite movies & store them in a list
name1=str(input("enter first movie name : "))
name2= str(input("enter second favorite movie name : "))
name3= str(input("Enter third favorite movie name : "))
list1=[]
list1.append(name1)
list1.append(name2)
list1.append(name3)
print(list1)


# WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
list2=[1, 'a', 'b', 1]
newlist=list2.copy()
print(newlist)
newlist.reverse()
print(newlist)
if(list2==newlist):
    print("list contains a palindrome of elements.")
else:
    print("list contains no palindrome of elements.")

# WAP to count the number of students with the "A" grade in the following tuple.
grade=('A', 'B', 'C', 'A', 'D', 'A', 'B','C')
print(type(grade))
print("Number of students with A grade are : ",grade.count('A'))

# WAP to sort the elements of the list
grade1=['A', 'B', 'C', 'A', 'D', 'A', 'B','C']
grade1.sort()
print(grade1)