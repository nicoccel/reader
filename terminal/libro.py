import os
import time

def nuovolibro():
    ok = False
    while ok == False:
        print("inserisci il nome del libro \ manga \ fumetto \ qualsiasi cosa sia")
        nome = input()
        print("inserisci il numero del volume o premi x se è un volume unico")
        num = input()
        if num == "x":
            numero = "volume unico"
        else:
            numero = num
        print("premi invio per confermare altrimenti premi un tasto")
        conferma = input()
        if conferma == "":
            ok = True
    return nome, numero

def visual_ind(lib):
    i = 0
    for l in lib:
        print(f"{i} - {l.nome}")
        i+=1
    return i
    


def toglilibro(lib):
    ok = False
    while ok == False:
        i = visual_ind(lib)
        print("inserisci l'indice del libro da togliere")
        try:
            ind = int(input())
            if ind == 0 or ind < i:
                lib.pop(ind)
                ok = True
                print("rimozione avvenuta con successo")
                time.sleep(1)
            else:
                print("indice non trovato\nriprovare premendo invio\nuscire premendo un tasto")
                ritenta = input()
                if ritenta != "":
                    ok = True
        except:
            print("errore valore inserito, riprovare o uscire premendo x\naltrimenti premi invio o un altro tasto")
            usc = input()
            if usc == "x":
                ok = True

    return lib


def modificalibro(lib):
    ok = False
    while ok == False:
        i = visual_ind(lib)
        print("inserisci l'indice del libro da modificare")
        try:
            ind = int(input())
            if ind == 0 or ind < i:
                print("premere invio per non modificare il dato")
                print("modifica nome")
                nom = input()
                print("modifica indice")
                indi = input()
                if nom != "":
                    lib[ind].nome = nom
                if indi != "":
                    lib[ind].numero = indi
                ok = True
                print("modifica avvenuta con successo")
                time.sleep(1)
            else:
                print("indice non trovato\nriprovare premendo invio\nuscire premendo un tasto")
                ritenta = input()
                if ritenta != "":
                    ok = True
        except:
            print("errore valore inserito, riprovare o uscire premendo x\naltrimenti premi invio o un altro tasto")
            usc = input()
            if usc == "x":
                ok = True

    return lib

    
        

class libro():
    def __init__(self, argv):
        self.nome = argv[0]
        self.numero = argv[1]

    def mostralibro(self):
        print("\n---------------------------------------------------------------------------------------------------------"
        + f"\nnome libro {self.nome}"
        + f"\nvolume libro {self.numero}"
        + "\n---------------------------------------------------------------------------------------------------------")