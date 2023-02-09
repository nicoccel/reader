import home
import registrazione
import accesso
import os
import os.path
import sys
import time
import subprocess
from threading import Thread
import libro
import utente
import cancellaconsole


#inizio codice PRINCIPALE CHE ESEGUE L'APPLICAZIONE
cancellaconsole.clearConsole()
#variabili_
azioneincorso = ""
esecuzione_program = True
accettazione_credenziali = False
#esecuzione
while esecuzione_program == True:
    cancellaconsole.clearConsole()
    accettazione_credenziali = False
    azioneincorso = home.aperturamenu()
    match(azioneincorso):
        case "1":
            credenziali_ut = accesso.accessocredenziali()
            if credenziali_ut == 0:
                print("errore")
                time.sleep(1)
            else:
                print("accesso in corso")
                time.sleep(1)
                accettazione_credenziali = True
                utente_activ = utente.utente()
                utente_activ.nuovo_utente(credenziali_ut[0],credenziali_ut[1],credenziali_ut[2])
        case "2":
            dati_registrazione = registrazione.nuovoaccount()
            utente_activ = utente.utente()
            libreria = []
            accettazione_credenziali = True
            utente_activ.nuovo_utente(dati_registrazione[0], dati_registrazione[1], dati_registrazione[2])
        case "3":
            print("chiusura progrmma in corso")
            esecuzione_program = False
            time.sleep(2)
            sys.exit()
    cancellaconsole.clearConsole()
    
    if accettazione_credenziali == True:
        esecuzione_profilo = True
        while esecuzione_profilo == True:
            azioneincorso = home.menuapp()
            match(azioneincorso):
                case "6":
                    utente_activ.mostradati_utente()
                case "1":
                    libreria.append(libro.libro(libro.nuovolibro(utente_activ.nome)))
                    print()
                case "2":
                    libreria = libro.toglilibro(libreria,utente_activ.nome)
                case "3":
                    libreria = libro.modificalibro(libreria, utente_activ.nome)
                case "4":
                    for obj in libreria:
                        obj.mostralibro()
                    print("premi invio per continuare")
                    invio = input()
                case "5":
                    utente_activ.modifica_impostazioni()
                case "e":
                    print("disconessione in corso ...")
                    esecuzione_profilo = False
                    time.sleep(2)
            cancellaconsole.clearConsole()
    cancellaconsole.clearConsole()