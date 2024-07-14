# single inheritance
"""
class A:
    varA = "first class variable"

class B(A): # inheritance is achieved in python by ()
    varB = "Second class variable"

obj = B()
print(obj.varA)
"""

# multilevel inheritance
"""
class A:
    varA = "first class variable"

class B(A): # inheritance is achieved in python by ()
    varB = "Second class variable"

class C(B):
    varC = "Third class variable"

obj = C()
print(obj.varA)
"""

# multiple inheritance
class A:
    varA = "first class variable"

class B: 
    varB = "Second class variable"

class C(A,B):
    varC = "Third class variable"

obj = C()
print(obj.varA)
print(obj.varB)