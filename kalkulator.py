import logging
logging.basicConfig(level=logging.DEBUG, format="")

#funkcja kalkulator

def kalkulator(dzialanie, liczby):
    if dzialanie == 1:
        #dodawanie
        wynik = liczby[0]
        for x in range(1, len(liczby)):
            wynik += liczby[x]
        return wynik
    elif dzialanie == 2:
        #odejmowanie
        wynik = liczby[0]
        for x in range(1, len(liczby)):
            wynik -= liczby[x]
        return wynik
    elif dzialanie == 3:
        #mnożenie
        wynik = liczby[0]
        for x in range(1, len(liczby)):
            wynik *= liczby[x]
        return wynik
    elif dzialanie == 4:
        #dzielenie
        wynik = liczby[0]
        for x in range(1, len(liczby)):
            wynik /= liczby[x]
        return wynik


#funkcja która tłumaczy nam operację w zależności jakie działanie wybierzemy
def info(dzialanie, liczby):
    if dzialanie == 1:
        text = "Dodaję "
        for i in range(len(liczby)-1):
            text = text + f"{liczby[i]} do "
        text = text + f"{liczby[len(liczby)-1]}"
        logging.debug(text)
    elif dzialanie == 2:
        text = "Odejmuję "
        for i in range(len(liczby)-1):
            text = text + f"{liczby[i]} od "
        text = text + f"{liczby[len(liczby)-1]}"
        logging.debug(text)
    elif dzialanie == 3:
        text = "Mnożę "
        for i in range(len(liczby)-1):
            text = text + f"{liczby[i]} razy "
        text = text + f"{liczby[len(liczby)-1]}"
        logging.debug(text)
    elif dzialanie == 4:
        text = "Dzielę "
        for i in range(len(liczby)-1):
            text = text + f"{liczby[i]} przez "
        text = text + f"{liczby[len(liczby)-1]}"
        logging.debug(text)

if __name__ == "__main__": 
    dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    tries = 5
    for i in range(6):
        #maxymalna ilość prób 5
        tries -= 1
        if tries < 0:
            print("Przekroczono maxymalną liczbę prób: 5")
            exit(1)
        #sprawdzamy czy zostały podane liczby oraz przecinki
        try:
            liczby = [int(x) for x in input("Proszę podać liczby po przecinkach: ").split(",")]
            #sprawdzamy czy zostały podane przynajmniej dwie liczby
            if len(liczby) == 1:
                print("Zbyt mało liczb aby wykonać zadanie - podaj minimum dwie liczby.")
                exit(1)
            break
        except ValueError:
            print("Proszę podać liczbę oraz używać tylko przecinków")
        


wynik = kalkulator(dzialanie, liczby)
info(dzialanie, liczby)
print(wynik)

