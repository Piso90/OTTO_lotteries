import random
import time

def generate_numbers():
    numeri = random.sample(range(1, 91), 6)
    numeri.sort()
    return numeri

def generate_superstar():
    superstar = random.randint(1, 90)
    return superstar

def generate_jolly():
    jolly = random.randint(1, 90)
    return jolly

def generate_numberslotto():
    numeri_lotto = random.sample(range(1, 91), int(quantinumeri))
    numeri_lotto.sort()
    return numeri_lotto

def generate_ruota():
    ruota = random.randint(1, 11)
    return ruota

def generate_numoro():
    numoro = random.randint(1, 90)
    return numoro

print("")
print("----LOADING_PROGRAM----")
print("")
time.sleep(1)
print("----CONNECTION_ESTABLISHED----")
print("")
time.sleep(1)
print("----STARTING----")
time.sleep(1)
print("")
nome = input("Dimmi il tuo nome per procedere: ")
print("")
print("Benvenuto",nome)
print("")
time.sleep(1)
print("<< INIZIO PROGRAMMA >>")
print("")
print("")
time.sleep(1)


# variabili
repeat = "y"
risposta = "y"
conta = 0

print("Ciao ", nome, ", a quale gioco voi partecipare?")
print("1. SUPERENALOTTO")
print("2. GIOCO DEL LOTTO")
print("")
gioco = input("Digita il numero del gioco corrispontente: ")
time.sleep(1)
print("")
print("")

try:
    tipogioco = int(gioco)
except:
    print("<< ERRORE - Input non valido! >>")
    print("")
    print("<< PROGRAMMA TERMINATO >>")
    quit()

#INIZIA GIOCO SUPERENALOTTO
if tipogioco == 1:
    while risposta.lower() == "y":
        numeri = generate_numbers()
        superstar = generate_superstar()
        jolly = generate_jolly()
        while superstar in numeri:
            #ricalcola superstar perchè uguale a uno dei 6 numeri
            superstar = generate_superstar()
        while jolly in numeri:
            #ricalcola jolly perchè uguale a uno dei 6 numeri
            jolly = generate_jolly()
        tutti = numeri.copy()
        tutti.append(jolly)
        #tutti è numeri + jolly su cui verificare superstar
        while superstar in tutti:
            #superstar è già presente, ricalcola
            superstar = generate_superstar()
            time.sleep(1)
        print("")
        print("Numeri quadro gioco:", numeri)
        print("Jolly:", jolly)
        print("Superstar:", superstar)
        conta = conta + 1
        # Conta quanti quadri forniti
        time.sleep(1)
        risposta = input("Vuoi completare un altro quadro? (y/n) ")
        time.sleep(1)
        if risposta.lower() != "y" and risposta.lower() != "n":
            print('Premere tasto Y per confermare o tasto N per negare. Altri input errati termineranno il programma')
            risposta = input("Vuoi completare un altro quadro? (y/n) ")
    print("")
    print("")
    if conta == 1:
        print(nome,", ti ho fornito", conta ,"quadro di gioco. Buona fortuna!")
    else: print(nome,", ti ho fornito", conta ,"quadri di gioco. Buona fortuna!")
    time.sleep(1)
    print("")
    print("")
    print("<< TERMINE PROGRAMMA >>")

#FINE GIOCO SUPERENALOTTO


#INIZIA GIOCO LOTTO

if tipogioco == 2:
    while repeat.lower() == "y":
        quantinumeriquestion = input("Quanti numeri vuoi giocare? ")
        try:
            quantinumeri = int(quantinumeriquestion)
        except:
            print("<< ERRORE - Input non valido >>")
            print("")
            time.sleep(1)
            print("<< PROGRAMMA TERMINATO >>")
            quit()
        if quantinumeri > 10:
            print('Inserire un numero da 1 a 10, in quantità massima consentita dal gioco. Altri input errati termineranno il programma')
            quantinumeriquestion = input("Quanti numeri vuoi giocare? ")
            quantinumeri = int(quantinumeriquestion)
            if quantinumeri > 10:
                print("")
                print("<< PROGRAMMA TERMINATO >>")
                quit()
        # inserire controllo input e nome
        time.sleep(1)
        conta = 0

        numeri_lotto = generate_numberslotto()

        #numoro = generate_numoro()

        risposta = input("Vuoi che ti indico in che ruota giocare? (y/n) ")
        time.sleep(1)
        if risposta.lower() != "y" and risposta.lower() != "n":
            print('Premere tasto Y per confermare o tasto N per negare. Altri input errati termineranno il programma')
            risposta = input("Vuoi che ti indico in che ruota giocare? (y/n) ")
        print("")
        time.sleep(1)
        if risposta.lower() == "y":
            ruota = generate_ruota()
            if ruota == 1:
                print("Bari")
            if ruota == 2:
                print("Cagliari")
            if ruota == 3:
                print("Firenze")
            if ruota == 4:
                print("Genova")
            if ruota == 5:
                print("Milano")
            if ruota == 6:
                print("Napoli")
            if ruota == 7:
                print("Palermo")
            if ruota == 8:
                print("Roma")
            if ruota == 9:
                print("Torino")
            if ruota == 10:
                print("Venezia")
            if ruota == 11:
                print("Ruota nazionale")
        print("")
        time.sleep(1)
        print(numeri_lotto)
        print("")
        print("")
        repeat = input("Vuoi giocare ancora? (y/n) ")
        time.sleep(1)
        if repeat.lower() != "y" and repeat.lower() != "n":
            print('Premere tasto Y per confermare o tasto N per negare. Altri input errati termineranno il programma')
            repeat = input("Vuoi giocare ancora? (y/n) ")
    print("")
    print("")
    print("Buona fortuna!")
    print("")
    time.sleep(1)
    print("<< TERMINE PROGRAMMA >>")

#FINE GIOCO LOTTO
if tipogioco == 0 or tipogioco >2:
    print("Il numero inserito non è corretto, il programma verrà terminato")
    print("")
    time.sleep(1)
    print("<< TERMINE PROGRAMMA >>")
quit()