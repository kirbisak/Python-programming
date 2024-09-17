# a=0
# b=1
# print(a, end=" ")
# while a < 300:
#   a,b = a+b, a
#   print(a, end=" ")


def binary(cislo):
    list1 = []
    while cislo >= 1:
        list1.append(cislo % 2)
        cislo = cislo // 2
    return list1[::-1]


def fizzybuzzy(number):
    for number in range(1, 51):
        if number % 5 == 0 and number % 3 == 0:
            print("Fizzbuzz")
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        else:
            print(number)

# def prime_number(n):
#     count = 0
#     for i in range(2,n):
#         if n % i == 0:
#             count += 1
#     if count == 0:
#         print("je prvocislo")
#     else:
#         print("nie je")

def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
        else:
            return True

print(ord("A") -55)