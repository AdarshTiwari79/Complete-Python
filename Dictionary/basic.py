# Dictionaries are used to store data values in key:value pairs 
# They are unordered, mutable(changeable) & don't allow duplicate keys
# keys are alway a non mutable type of data
# values can be of mutable or nonmutable both

dict={
    'name':'Adarsh Tiwari',
    'percentage': 82,
    'marks': [83,92,71]
}
print(dict['name'])
print(dict)
dict['name']="Saurav" # inserting values in corresponding key
print(dict['name'])


# Nested dictionary concept can be achieved via taking a value as dictionary

student={
    "name":"Adarsh Tiwari",
    "subject" : {
        "physics":99,
        "chemistry": 89,
        "maths":82
    },
    "village": "Ramput",
}

print(student)
print(student["subject"]["physics"])
student['subject']['chemistry']='fail'
print(student['subject']['chemistry'])