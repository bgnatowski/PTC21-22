# STAŁE
LICZBA_DO_DODANIA_DO_RESZTY_ABY_OTRZYMAC_ZNAK_ASCII_DLA_RESZT_WIEKSZYCH_OD_9 = 55
MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU = 10
MIN_PODSTAWA = 2
MAX_PODSTAWA = 36
MAX_ZAKRES_LICZBY = 20
#####################


# dziala aktualnie:
# z wiekszej (do 10) na mniejszą
# z wiekszej (od 10) na mniejsza
def wczytajPodstaweWejsciowa():
    podstawa = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    while podstawa < MIN_PODSTAWA or podstawa > MAX_PODSTAWA:
        print('Błedna podstawa!')
        podstawa = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    return podstawa


# sprawdza czy podana liczba w systemie > 10 używa odpowienich dla siebie liter sys(11) do A, sys(12) do B
# sys(13) do C, sys(14) do D .... sys(36) do Z
def isCorrectForBase(liczba, podstawa):
    # narazie zwracam true jako iż zakladam ze wprowadzona liczba nie bedzie zawierać niepoprawnych znakow
    return True


def wczytajLiczbeOPodstawie(podstawa):
    while True:
        if podstawa <= MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczba = int(input(f'Podaj liczbe w systemie ({podstawa}):'))
            return liczba
        elif podstawa > MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczba = input(f'Podaj liczbe w systemie ({podstawa}):')
            if isCorrectForBase(liczba, podstawa):
                return liczba


def wczytajPodstaweWynikowa(podstawaWej):
    podstawa = int(input(f'Podaj podstawę liczby wynikowej: (2-36) bez ({podstawaWej}): '))
    while podstawa < MIN_PODSTAWA or podstawa > MAX_PODSTAWA or podstawa == podstawaWej:
        print('Błedna podstawa!')
        if podstawa == podstawaWej:
            print(f'Po co przeliczać liczbę o podstawie ({podstawaWej}) na te samą?')
        podstawa = int(input(f'Podaj podstawę liczby wynikowej (2-36) bez ({podstawaWej}): '))

    return podstawa

#dziala przez podstaawe 10
def zmienModulo(liczba, podstawaWyj):
    reszty = []
    while liczba != 0:
        reszta = liczba % podstawaWyj
        if reszta >= MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            reszty.append(chr(reszta + LICZBA_DO_DODANIA_DO_RESZTY_ABY_OTRZYMAC_ZNAK_ASCII_DLA_RESZT_WIEKSZYCH_OD_9))
        else:
            reszty.append(str(reszta))
        print(f'{liczba} / {podstawaWyj} = {liczba // podstawaWyj} reszta {reszta}')
        liczba = liczba // podstawaWyj
    reszty.reverse()
    return "".join(reszty)


def znakNaLiczbe(znak):
    if znak.isdigit():
        wartoscLiczby = int(znak)
    elif 'a' <= znak.lower() <= 'z':
        wartoscLiczby = ord(znak.lower()) - ord('a') + 10
    return wartoscLiczby


def konwertujLiczbeNaZnaki(liczba):
    znaki = []
    dlugoscLiczby = len(liczba)

    for i in range(dlugoscLiczby):
        znaki.append(znakNaLiczbe(liczba[i]))
    return znaki


def konwertujNaWartosc(liczba, podstawaWej):
    znakiWLiczbie = konwertujLiczbeNaZnaki(liczba)
    dlugoscLiczby = len(liczba)

    suma = 0
    for i in range(dlugoscLiczby):
        dlugoscLiczby -= 1
        wartosc = znakiWLiczbie[i] * (podstawaWej ** dlugoscLiczby)
        suma += wartosc
        print(f'{i}. znak to {liczba[i].upper()} ({znakiWLiczbie[i]}*{podstawaWej}^{dlugoscLiczby})')
    print(f'Suma = {suma}')
    return suma


def main():
    while True:
        print('***Program do przeliczania liczby pomiędzy dwoma systemami liczbowymi***\n')

        podstawaWej = wczytajPodstaweWejsciowa()
        liczba = wczytajLiczbeOPodstawie(podstawaWej)
        podstawaWyj = wczytajPodstaweWynikowa(podstawaWej)

        if podstawaWej <= MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczbaWynikowa = zmienModulo(liczba, podstawaWyj)
        elif podstawaWej > MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczbaWynikowa = konwertujNaWartosc(liczba, podstawaWej)
        print(f'Liczba {liczba}({podstawaWej}) = {liczbaWynikowa}({podstawaWyj})')

        wybor = input('Chcesz przeliczyć jeszce raz (y/n): ')
        if wybor == 'n':
            print("Koniec.")
            break
        else:
            print('\n')
            continue


if __name__ == '__main__':
    main()
