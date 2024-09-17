import random

print("Pre ukoncenie stlac 0")
res = 1
right = 0
all = 0
while True:
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    res = int(input(f"Kolko je {x}*{y} ="))
    if res == 0:
        break
    if res == x * y:
        right += 1
        print("Spravne")
    else:
        print("Nespravne")
    all += 1
print(f"Tvoje skore {right}/{all} = {round((right/all)*100, 2)}%")
