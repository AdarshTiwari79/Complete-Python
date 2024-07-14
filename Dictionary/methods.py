student={
    "name":"Adarsh Tiwari",
    "subject" : {
        "physics":99,
        "chemistry": 89,
        "maths":82
    },
    "village": "Ramput",
}

# dict.keys() -> returns all keys of primary dictionary

print(len(student))
print(student.keys())
list1=list(student.keys()) # type casting the returned key elements into list
print(list1)

# dict.values() -> returns all values of dictionary
print(student.values())
print(list(student.values())) # type casting the returned value elements into list
print(len(student))
print(len(student.values()))

# dict.items() -> returns all (key, value) pairs as tuples
print(student.items())
tup2=student.items()
print(type(tup2))

# dict.get("key") -> Returns the key according to value
print(student.get("name"))

# dict.update(newDict) -> inserts the specific items to the dictionary
print("From here update method is executing")
topper={"name": "Adarsh Tiwari", "age" :"22"}
student.update(topper) # updating through a new dictionary (preferred way)
print(student)

student.update({"city": "Jaunpur"}) # updating via directly passing key: value pair
print(student)