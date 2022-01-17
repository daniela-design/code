import random
from ai import tah_pocitace
from utils import tah

symbol = "x"
symbol_pocitace = "o" 

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole):
    while True:
        pozice = int(input("Na kterou pozici chceš hrát? "))
        if pozice < 0:
            print("Zadej kladné číslo!")
        elif pozice >= len(pole):
            print("Políčko je mimo pole!")
        elif pole[pozice] != "-":
            print("Políčko je obsazené!")
        else:
            return tah(pole, pozice, symbol)
        
def piskvorky1d():
    pole = "--------------------"   
    kolo = 1
    while True:
        pole = tah_hrace(pole)
        if vyhodnot(pole) != "-":
            break

        pole = tah_pocitace(pole, symbol_pocitace)
        if vyhodnot(pole) != "-":
            break

        print(f"{kolo}. kolo: {pole}")
        kolo += 1

    hodnoceni = vyhodnot(pole)
        
    if hodnoceni == "x":
        return "Vyhrál jsi!"
    elif hodnoceni == "o":
        return "Prohrál jsi!"
    elif hodnoceni == "!":
        return "Remíza"

def strategie_pocitace(pole):
    if "oo" in pole:
        if pole.index("oo") == len(pole):
            return tah(pole, pole.index("oo", -1), "o")
        else:
            return tah(pole, pole.index("oo", 1), "o")
    elif "xx" in pole:
        if pole.index("xx") == len(pole):
            return tah(pole, pole.index("xx", 1), "o")
        else:
            return tah(pole, pole.index("xx", 1), "o")
    elif "o" in pole:
        return tah(pole, pole.index("o", 1), "o")