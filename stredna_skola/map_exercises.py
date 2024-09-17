numbers = [10, 20, 30, 40, 50, 60]
indexes = [1, 2, 3, 4, 5, 6]

a = list(map(lambda x, y: x**y, numbers, indexes))

myList = ['f', 'b', 'U', 'i', 'o', 'E', 'a']

def func(x):
    return (x.upper(), x.lower())

b = list(map(lambda x: func(x), myList))
print(b)
