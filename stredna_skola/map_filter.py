#https://www.w3resource.com/python-exercises/map/index.php

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
       #12, 15, 18

# x = list(map(lambda a, b, c: a + b + c, list1, list2, list3))
# print(x)

def func(x):
    return x%2 != 0 

def add5(x):
    return x + 5

myList = [1, 2, 3, 4, 5, 6, 7, 8]
          
a = list(filter(func, myList))
b = list(map(add5, filter(func, myList)))
c = list(filter((lambda x: x > 5), myList))


# https://realpython.com/python-kwargs-and-args/

def myFunc(*args):
    result = 0
    for i in args:
        result += i
    return result

# print(myFunc(*myList))

myDict = {"a": "Ahoj", "b": "Cau", "c": "Servus"}

def myFunc2(**kwargs):
    res = ""
    for i in kwargs.values():
        res += i
    return res

# print(myFunc2(**myDict))

years = [14, 16, 17, 21, 25, 45]

# def myFunc3(x):
#     if x < 18:
#         return False
#     else:
#         return True
    
adults = filter(lambda x: x < 18, years)




