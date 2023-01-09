import os
import time


def accessocredenziali( ):
    coretto = False
    while coretto == False:
        print("bentornato :)")
        print("inserisci la tua mail")
        in_mail = input()
        print("inserisci la tua password del tuo account")
        in_password = input()
        
        #verrà aperto il file delle credenziali e verranno chiestri i dati dal database e se corrispondono avviene l'accesso altrienti si 
        #può tornare indietro al menù principale
        
        
        in_utente = ""
        try:
            f = open(f"{os.getcwd()}\\credenziali\\{in_mail}-credenziali.txt", "r")
            r_cred = f.read().split('|')
            f.close()
            #print(r_cred)
            if r_cred[1] == in_mail and r_cred[2] == in_password:
                print("accesso in corso")
                time.sleep(1)
                return r_cred
        except:
            print("errore credenziali")

        return 0