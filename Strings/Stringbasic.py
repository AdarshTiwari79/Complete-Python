# escape sequence characters are used to formatting the sentences they are \n,\t etc.

str1="This is Adarsh Tiwari. \n I am from mumbai. \n Are you Somaliya?"
print(str1)

# Concatenation = addition of two string 

str2 = "Adarsh"
str3 = "Tiwari"
concate=str2+" "+str3
print(concate)

# length of the string
print(len(str2))

# indexing : idexes are assigned to the characters of the string 
# python has a special feature of assigning negative indexing for back track of characters

str4= "Hello World"
print(str4[-1])
print(str4[6])

# slicing : means accesing a portion of string. Very useful while studying ML(machine learning)
# syntax explaination: string_name[start_index:last_index] string will print from start index and (last_index-1)
print(str4[3:5])