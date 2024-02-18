from functools import reduce

def is_even(n): #compulsorily this function should return boolean
    return n%2 == 0

def doubles(n):
    return n*2

def add_all(a,b): #will always take 2 arguments
    return a+b

nums = [3,5,6,7,2]
even_nums1 = list(filter(is_even,nums))
even_nums = list(filter(lambda n : n%2==0,nums))
# print(even_nums)

doubles1 = list(map(doubles, even_nums))
doubles = list(map(lambda n : n*2, even_nums))
print(type(doubles))
# print(doubles)

sum1 = reduce(add_all,doubles)
sum = reduce(lambda a,b : a+b,doubles)
print(sum)