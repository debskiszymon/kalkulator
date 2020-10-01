import logging
logging.basicConfig(level=logging.DEBUG, format="")

def kalkulator(dzialanie, liczba_01, liczba_02):
    wynik = 0
    if dzialanie == 1:
        wynik = liczba_01 + liczba_02
    elif dzialanie == 2:
        wynik = liczba_01 - liczba_02
    elif dzialanie == 3:
        wynik = liczba_01 * liczba_02
    elif dzialanie == 4:
        wynik = liczba_01 / liczba_02
    return wynik    

#print(kalkulator(4, 2, 2))

if __name__ == "__main__": 
    dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    liczba_01 = int(input("Podaj składnik 1:"))
    liczba_02 = int(input("Podaj składnik 2:"))
    if dzialanie == 1:
        logging.debug(f"Dodaję {liczba_01} do {liczba_02}")
    elif dzialanie == 2:
        logging.debug(f"Odejmuję {liczba_01} od {liczba_02}")
    elif dzialanie == 3:
        logging.debug(f"Mnożę {liczba_01} razy {liczba_02}")
    elif dzialanie == 4:
        logging.debug(f"Dzielę {liczba_01} przez {liczba_02}")
    print(kalkulator(dzialanie, liczba_01, liczba_02))
