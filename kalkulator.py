import logging
logging.basicConfig(level=logging.DEBUG, format="")

def dodwanie(*argv):
    wynik = 0
    for arg in argv:
        wynik += arg
    return wynik
def odejmowanie(*argv):
    wynik = 0
    for arg in argv:
        wynik -= arg
    return wynik
def mnozenie(*argv):
    wynik = argv[0]
    for x in range(1, len(argv)):
        wynik *= argv[x]
    return wynik
def dzielenie(*argv):
    wynik = argv[0]
    for x in range(1, len(argv)):
        wynik /= argv[x]
    return wynik

#calculator function

def kalkulator(dzialanie, *argv):
    wynik = 0
    if dzialanie == 1:
        wynik = dodwanie(argv)
    elif dzialanie == 2:
        wynik = liczba_01 - liczba_02
    elif dzialanie == 3:
        wynik = liczba_01 * liczba_02
    elif dzialanie == 4:
        wynik = liczba_01 / liczba_02
    return wynik    

#is the input a integer check function

def is_int():
    while True:
            try:
                liczba = int(input("Podaj składnik 1:"))
                return liczba             
            except ValueError:
                print("Proszę podać liczbę!!")

#print(kalkulator(4, 2, 2))

if __name__ == "__main__": 
    dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    liczba_01 = is_int()
    liczba_02 = is_int()
    if dzialanie == 1:
        logging.debug(f"Dodaję {liczba_01} do {liczba_02}")
    elif dzialanie == 2:
        logging.debug(f"Odejmuję {liczba_01} od {liczba_02}")
    elif dzialanie == 3:
        logging.debug(f"Mnożę {liczba_01} razy {liczba_02}")
    elif dzialanie == 4:
        logging.debug(f"Dzielę {liczba_01} przez {liczba_02}")
    print(kalkulator(dzialanie, liczba_01, liczba_02))
