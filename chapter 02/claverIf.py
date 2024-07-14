# syntax for the claver if ternary operator is var=(false value, true value)[condition]

age=int(input("age : "))
vote=("yes","no")[age<18]
print(vote)

salary=float(input("salary : "))
tax=salary*(0.1,0.2)[salary>=50000]
print(tax)