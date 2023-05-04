
idnum = input("Zadaj platne rodne cislo: ").replace("/", "")

def rodne_cislo(id):
    pohlavie = None
    year = idnum[0:2]
    month = idnum[2:4]
    day = idnum[4:6]
    
    if int(month) > 50:
        month = int(month) - 50
        pohlavie == "zena"
    else:
        pohlavie =="muz"

    print(f"{pohlavie} s rodnym cislo {day}.{month}.{year}")
rodne_cislo(idnum)
