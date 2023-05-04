import os

def kvadraticka(a, b ,c):
    d = (b**2 - 4 * a * c)
    if d > 0:
        x1 = (-b + (d)**0.5) / 2 * a
        x2 = (-b - (d)**0.5) / 2 * a
        return x1, x2
    elif d == 0:
        x = -b / 2*a
        return x
    else:
        print("?")

# if not os.path.exists("kvadraticka.txt"):
#     print("Subor neexistuje")
# else:
#     with open("kvadraticka.txt.txt", "r") as f:
#         for line in f:
#             print(line)

lst = [1, 2, -3]


print(kvadraticka(*lst))