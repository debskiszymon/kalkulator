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

print(kalkulator(4, 2, 2))
        