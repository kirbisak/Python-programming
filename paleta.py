import os
import random

if not os.path.exists("obrazok.txt"):
    print("nic")
else:
    colours = []
    with open("obrazok.txt", "r") as f:
        for line in f:
            for element in line.split(" "):
                colours.append(element)

def palet():
    paleta = set()
    for element in colours:
        if element not in paleta:
            paleta.add(element)
    return len(paleta)

def komp():
    i = 1
    while 2**i < palet():
        i += 1
    else:       
        return round((24-i)*100/24, 0)
        
print(komp())