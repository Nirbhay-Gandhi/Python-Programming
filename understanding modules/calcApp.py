import mymath

"""
concept of importing any module: while importing any module, it executes the module also 
at the same time. 
We want this module to exectes only functions, not all other stuffs.
So, to create this we make use of __name__ keyword

value of __name__ when executed in it's own file, is "main()"
When imported in some other file and executed, then it takes the value
"""
print("name in calcApp ",__name__)
num1,num2 = 5,10
print(f"adding {num1} + {num2} = {mymath.add(num1, num2)}")
print(f"subtracting {num1} - {num2} = {mymath.sub(num1, num2)}")
