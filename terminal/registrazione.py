import os


def nuovoaccount():
    print("benvenuto nella nostra app per catalogare i tuoi libri, fumetti, manga, o tutto quello che ti piace legere")
    print("prima di tutto inserisci il tuo nome utente : ")
    in_nomeutente = input()
    print("inserisci una tua mail :")
    in_mail = input()
    print("inserisci una password :")
    in_password = input()
    #creazione del file per salvare le credenziali sul dispositivo e successivamente salvarle su un database
    dir = os.getcwd()
    path = "credenziali"
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(f"{dir}\\{path}\\{in_mail}-credenziali.txt", "w")
    f.write(f"{in_nomeutente}|{in_mail}|{in_password}")
    f.close()
    return in_nomeutente,in_mail,in_password