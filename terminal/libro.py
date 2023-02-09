import os
import time
import cancellaconsole

def filelibronuovo(nomem,num,n):
    dir = os.getcwd()
    lib = "libreria"
    try:
        if not os.path.exists(n):
            os.makedirs(f"{dir}\\{lib}\\{n}")
    except:
        print()
    f = open(f"{dir}\\{lib}\\{n}\\{nomem}.txt", "w")
    f.write(f"{nomem}||{num}")
    f.close()

def filelibrotogli(n,nn):
    os.remove(os.getcwd()+"\\libreria\\"+nn+"\\"+n+".txt")


def filelibromodifica(n,nn):
    print()

def nuovolibro(nomem):
    path = "libreria"
    if not os.path.exists(path):
        os.makedirs(path)
    ok = False
    while ok == False:
        cancellaconsole.clearConsole()
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
            filelibronuovo(nome,numero,nomem)
    return nome, numero

def visual_ind(lib):
    i = 0
    for l in lib:
        print(f"{i} - {l.nome}")
        i+=1
    return i
    


def toglilibro(lib,nn):
    ok = False
    while ok == False:
        cancellaconsole.clearConsole()
        i = visual_ind(lib)
        if i != False:
            print("inserisci l'indice del libro da togliere")
            try:
                ind = int(input())
                if ind == 0 or ind < i:
                    n = lib[ind].nome
                    lib.pop(ind)
                    ok = True
                    print("rimozione avvenuta con successo")
                    time.sleep(1)
                    filelibrotogli(n,nn)
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
        else:
            print("non hai elementi nella tua libreria")
            time.sleep(1) 
            ok = True

    return lib


def modificalibro(lib, n):
    ok = False
    while ok == False:
        cancellaconsole.clearConsole()
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
                filelibromodifica(n, nom, indi)
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