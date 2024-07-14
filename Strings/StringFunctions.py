# str.endswith("substring") -> returns true if string endds with substring

str1="hi this is python tutorial string function module."
check=str1.endswith("ule.")
print(check)

# str.capitalize() -> used to convert the first letter of the string into Capital form 
# Doesnot perform direct modification in original string replicate the string and do capitalization

print(str1.capitalize())
print("Original String : ",str1)

# str.replace(old, new) -> Replaces all occurances of the old substrings with new subString

print(str1.replace("i","e"))

# str.find(word) -> returns the first index of the first occurance of the word or substring 

print(str1.find("this"))

# str.count(word) -> counts the number of occurances of the word

print(str1.count("is"))