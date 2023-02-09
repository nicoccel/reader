import time
import cancellaconsole

class utente():
    def __init__(self):
        self.nome = " "
        self.mail = " "
        self.password = " "

    def nuovo_utente(self, n, m, p):
        self.nome = n
        self.mail = m
        self.password = p

    def carica_utente(self):
        print()

    def modifica_utente(self):
        print()

    def mostradati_utente(self):
        cancellaconsole.clearConsole()
        print("i tuoi dati sono :"
        + f"\nnome {self.nome}"
        + f"\nmail {self.mail}"
        + f"\npassword privata")
        print(self.password)
        print("premi inviob o un'altro tasto per continuare")
        invio = input()

    def modifica_impostazioni(self):
        cancellaconsole.clearConsole()
        print("seleziona che impostazione cambiare")
        print("1 cambia password")
        print("2 cambia mail")
        print("3 cambia nome utente")
        azione = input()
        match(azione):
            case "1":
                self.cambio_password()
            case "2":
                self.cambio_mail()
            case "3":
                self.cambio_nomeutente()

    def cambio_password(self):
        cancellaconsole.clearConsole()
        ok = False
        while ok == False:
            cancellaconsole.clearConsole()
            print("inserisci la nuova password")
            passw = input()
            print("conferma passowrd")
            passwconf = input()
            if passw == passwconf:
                print("cambio password corretto")
                ok = True
                self.password = passw
                time.sleep(1)
            else:
                print("le password non corrispondono\nriprovare premendo invio")
                print("altrimenti premi un tasto per uscire")
                az = input()
                if az != "":
                    print("cambio password annullato")
                    time.sleep(1)
                    ok = True

    def cambio_mail(self):
        ok = False
        while ok == False:
            cancellaconsole.clearConsole()
            print("inserisci la nuova mail")
            ml = input()
            print("reinserisci la mail")
            mlconf = input()
            if ml == mlconf:
                self.mail = ml
                print("mail cambiata con successo")
                ok = True
                time.sleep(1)
            else:
                print("le mail non corrispondono\nreinserire premendo invio")
                print("altrimenti premi un tasto per uscire")
                az = input()
                if az != "":
                    print("cambio mail anullato")
                    time.sleep(1)
                    ok = True

    def cambio_nomeutente(self):
        ok = False
        while ok == False:
            cancellaconsole.clearConsole()
            print("inserisci il nuovo nome utente")
            nome = input()
            print("reinscerisci il nuovo nome")
            nomerein = input()
            if nome == nomerein:
                self.nome = nome
                ok = True
                print("cambio nome avvenuto con successo")
                time.sleep(1)
            else:
                print("errore inserimento \nreinserire premendo invio")
                print("altrimenti premi un tasto per uscire")
                az = input()
                if az != "":
                    print("cambio nome anullato")
                    time.sleep(1)
                    ok = True
