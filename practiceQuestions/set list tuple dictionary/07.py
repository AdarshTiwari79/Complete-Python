# Store the following word meanings in a python dictionary:
# table: "a piece of furniture","list of facts & figures"
# cat: "a small animal"

"""

mydictionary={
    "table":["a piece of furniture","list of facts & figures"],
    'cat': 'a small animal',
}

print(mydictionary)
"""

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# 'python','java','c++', 'python','javascipt', 'java','python', 'java','c++','c'

"""
subjects=['python','java','c++', 'python','javascipt', 'java','python', 'java','c++','c']
classroom=set(subjects)
print("classroom needed : ",len(classroom))
"""

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value

"""
exam={}
sub1={"phy":int(input('Enter physics marks : '))}
exam.update(sub1)
print("current dictionary is : ",exam)
sub2={"chem":int(input('Enter chemistry marks : '))}
exam.update(sub2)
print("current dictionary is : ",exam)
sub3={"maths": int(input('Enter mathematics marks : '))}
exam.update(sub3)
print("current dictionary is : ",exam)
"""

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

set1={9,str(9.0)} # one way
print(set1)

set2={('int',9),('float',9.0)}
print(set2)
