# import random

# def prime_number(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def sieve(n):
#     sieve = []
#     lst = [i for i in range(n+1)]
#     for element in lst:
#         if prime_number(element):
#             sieve.append(element)

#     return sieve

# print(sieve(17))


def prime(n):
    is_prime = True
    if n <= 1:
        is_prime = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def sieve(n): #n = 17
    lst = [i for i in range(n+1)]
    sito = []
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    # for i in range(n+1):
    #       lst.append(i)
    for element in lst:
        if prime(element):
            sito.append(element)
            # lst = [2, 3, 5, 7, 11, 13, 17]
    return sito

print(sieve(17))


# number = int(input("Zadaj cislo"))
# if prime(number):
#     print(f"tvoje cislo {number} je prvocislo, sito do tohto cisla {sieve(number)}")



