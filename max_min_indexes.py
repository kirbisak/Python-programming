import random
list1 = [random.randint(0, 100) for i in range(100)]
adresa = (int(input("Zadaj adresu: ")))

print(list1)
def min():
    min = 1000
    for i in range(len(list1)):
        if min > list1[i]:
            min = list1[i]
            imin = i
    return min, imin

def max():
    max = 0
    for i in range(len(list1)):
        if max < list1[i]:
            max = list1[i]
            imax = i
    return max, imax

A = min()
B = max()

print(f"minimum na adrese {(A[1] * 28) + adresa} je {A[0]}")
print(f"minimum na adrese {(B[1] * 28) + adresa} je {B[0]}")