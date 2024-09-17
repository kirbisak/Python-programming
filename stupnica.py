import random

def stupnica(n, k):
    list1 = [0, 0, 0, 0, 0]
    #        1, 2, 3, 4, 5 - znamky
    for i in range(n):
        k_random = random.randint(0, k)
        if 100 >= (k_random / k) * 100 >= 90:
            list1[0] += 1
        elif 90 > (k_random / k) * 100 >= 75:
            list1[1] += 1
        elif 75 > (k_random / k) * 100 >= 50:
            list1[2] += 1
        elif 50 > (k_random / k) * 100 >= 30:
            list1[3] += 1
        elif 30 > (k_random / k) * 100 >= 0:
            list1[4] += 1
    for i in range(len(list1)):
        print(f"ziakov ktori dostali {i + 1} bolo {list1[i]}")


def pisomka(n, k):
    list1 = [1, 2, 3, 4, 5]
    for i in range(n):
        k_random = random.randint(0, k)
        if 100 >= (k_random / k) * 100 >= 90:
            print(f"{k_random}bodov = 1", end=', ')
        elif 90 > (k_random / k) * 100 >= 75:
            print(f"{k_random}bodov = 2", end=', ')
        elif 75 > (k_random / k) * 100 >= 50:
            print(f"{k_random}bodov = 3", end=', ')
        elif 50 > (k_random / k) * 100 >= 30:
            print(f"{k_random}bodov = 4", end=', ')
        elif 30 > (k_random / k) * 100 >= 0:
            print(f"{k_random}bodov = 5", end=' ')
    print()
    print(f"{k * 1} - {k * 0.9} = 1")
    print(f"{k * 0.89} - {k * 0.75} = 2")
    print(f"{k * 0.74} - {k * 0.5} = 3")
    print(f"{k * 0.49} - {k * 0.3} = 4")
    print(f"{k * 0.29} - {k * 0}   = 5")

pisomka(5, 20)