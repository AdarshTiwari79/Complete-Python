# syntax for if-elif-else
# Python uses indentation instead of {} for if elif statements
# Indentation is proper spacing 

"""
light=input("Enter the color of the traffic light(in lowercase) : ")
if(light=="red"):
    print("Stop")
    print("Wait for signal to be green to go.")
elif(light=="yellow"):
    print("lookout")
elif(light=="green"):
    print("Go")
else:
    print("light is broken")

"""
"""
marks=int(input("Enter marks to know the grade : "))
if(marks>=90):
    print("your grade is A")
elif(marks>=80 and marks<90):
    print("Your grade is B")
elif(marks>=70 and marks<80):
    print("Your grade is C")
else:
    print("Your grade is D")
"""

A = int(input("A : "))
G = input("M/F : ")
if((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif((A==3 or A==4) and G=="F"):
    print('feee is 200')
elif(A==5 and G=="M"):
    print("fee is 300")
else:
    print("no fee")