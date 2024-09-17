import random

def myslim_si_cislo():
    number = random.randint(1, 100)
    pocitadlo = 0
    while True:
        pocitadlo += 1   
        guess = int(input(("Zadaj cislo: ")))
        if pocitadlo == 8:
            print("GAMEOVER")
            break
        elif guess > number:
            print("Hladane cislo je mensie")
        elif guess < number:
            print("Hladane cislo je vacsie")
        else:
            print(f"spravne, mal si na to {pocitadlo} pokusov")
            break
     

myslim_si_cislo()
