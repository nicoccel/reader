def aperturamenu():
    in_apertura = ""
    conferma_appertura = False
    while conferma_appertura == False:
        print("Benvenuto :)")
        print("digitare\n"
        + "\t 1 per accedere | 2 per registrarti | 3 esci")
        in_apertura = input()
        if in_apertura == "1":
            conferma_appertura = True
            #m,p,n = accessocredenziali()
            
        if in_apertura == "2":
            conferma_appertura = True
            #n, m = registrazione.nuovoaccount()

        if in_apertura == "3":
            conferma_appertura = True

        if conferma_appertura == False:
            print("input non valido" + "\nreinserire")

    return in_apertura


def menuapp():
    controllo_menu = False
    while controllo_menu == False:
        print("menù principale")
        print("premere : ")
        print("- 1 aggiungi nuovo contenuto alla tua libreria"
        + "\n- 2 togli elemento dalla tua libreria"
        + "\n- 3 modifica elemento esistente"
        + "\n- 4 visualizza la tua libreria completa"
        + "\n- 5 modifica impostazioni"
        + "\n- 6 visualizza i tuoi dati"
        + "\n- e uscire")
        in_opzione = input()
        if in_opzione == "1" or in_opzione == "2" or in_opzione == "3" or in_opzione == "4" or in_opzione == "5" or in_opzione == "e" or in_opzione == "6": controllo_menu = True 
        if controllo_menu == False: print("input inserito è invalido" + "\nreinserire")

    return in_opzione