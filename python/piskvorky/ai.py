import random
from utils import tah

# symbol_pocitace = "o"   


def tah_pocitace(pole, symbol_pocitace):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    delka_pole = len(pole)
    zbyvajici_pokusy = delka_pole * 5
    while zbyvajici_pokusy > 0:
        pozice_pocitace = random.randint(0, delka_pole) 
        if pole[pozice_pocitace] == "-":
            break
        zbyvajici_pokusy = zbyvajici_pokusy -1
        
    return tah(pole, pozice_pocitace, symbol_pocitace)