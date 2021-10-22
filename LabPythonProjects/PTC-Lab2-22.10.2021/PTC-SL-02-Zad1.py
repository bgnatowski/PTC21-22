# STAŁE
LICZBA_DO_DODANIA_DO_RESZTY_ABY_OTRZYMAC_ZNAK_ASCII_DLA_RESZT_WIEKSZYCH_OD_9 = 55
MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU = 10
MIN_PODSTAWA = 2
MAX_PODSTAWA = 36
#####################


def getInputBase():
    podstawa = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    while podstawa < MIN_PODSTAWA or podstawa > MAX_PODSTAWA:
        print('Błedna podstawa!')
        podstawa = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    return podstawa


# TODO
def isCorrectForBase(liczba, podstawa):
    # sprawdza czy podana liczba w systemie > 10 używa odpowienich dla siebie liter sys(11) do A, sys(12) do B
    # sys(13) do C, sys(14) do D .... sys(36) do Z
    # narazie zwracam true jako iż zakladam ze wprowadzona liczba nie bedzie zawierać niepoprawnych znakow
    return True


def getNumberInBase(podstawa):
    while True:
        if podstawa <= MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczba = input(f'Podaj liczbe w systemie ({podstawa}):')
            return liczba
        elif podstawa > MIN_PODSTAWA_BEZ_ZNAKOW_ALFABETU:
            liczba = input(f'Podaj liczbe w systemie ({podstawa}):')
            if isCorrectForBase(liczba, podstawa):
                return liczba


def getOutputBase(podstawaWej):
    podstawa = int(input(f'Podaj podstawę liczby wynikowej: (2-36) bez ({podstawaWej}): '))

    while (MIN_PODSTAWA > podstawa < MAX_PODSTAWA) or (podstawa == podstawaWej):
        print('Błedna podstawa!')
        if podstawa == podstawaWej:
            print(f'Po co przeliczać liczbę o podstawie ({podstawaWej}) na tą samą?')

        podstawa = int(input(f'Podaj podstawę liczby wynikowej (2-36) bez ({podstawaWej}): '))

    return podstawa


def dec2other(liczba, podstawaWyj):
    liczba = int(liczba)
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


def getValue(znak):
    if znak.isdigit():
        value = int(znak)
    elif 'a' <= znak.lower() <= 'z':
        value = ord(znak.lower()) - ord('a') + 10
    return value


def getValuesOf(liczba):
    values = []
    dlugoscLiczby = len(liczba)

    for i in range(dlugoscLiczby):
        charValue = getValue(liczba[i])
        values.append(charValue)
    return values


def other2dec(liczba, podstawaWej):
    wartosciZnakowLiczby = getValuesOf(liczba)
    dlugoscLiczby = len(liczba)
    liczbaW10 = 0

    # liczaW10 = a_0 * p^n + a_1 * p^n-1 + a_m * p^m
    for i in range(dlugoscLiczby):
        dlugoscLiczby -= 1
        znak = liczba[i].upper()
        wartoscZnaku = wartosciZnakowLiczby[i]
        liczbaW10 += wartoscZnaku * (podstawaWej ** dlugoscLiczby)
        print(f'{i}. znak to {znak} ({wartoscZnaku}*{podstawaWej}^{dlugoscLiczby})')

    print(f'Liczba {liczba}({podstawaWej}) w sys 10 = {liczbaW10}')
    print('Teraz nastąpi przeliczenie na liczbe na zadaną podstawie wyjściowa:')
    return liczbaW10


def main():
    while True:
        print('***Program do przeliczania liczby pomiędzy dwoma systemami liczbowymi***\n')

        inputBase = getInputBase()
        inputNumber = getNumberInBase(inputBase)
        outputBase = getOutputBase(inputBase)

        numberIn10 = other2dec(inputNumber, inputBase)

        # wyłapanie liczby 0
        if numberIn10 == 0:
            outputNumber = '0'
        else:
            outputNumber = dec2other(numberIn10, outputBase)

        print(f'Liczba {inputNumber}({inputBase}) = {outputNumber}({outputBase})')

        choice = input('Chcesz przeliczyć jeszce raz (y/n): ')
        if choice == 'n':
            print("Koniec.")
            break
        else:
            print('\n')
            continue


def tests():
    print('TESTY')
    # test 1
    assert other2dec("1010", 2) == 10
    assert other2dec('1252', 8) == 682
    assert other2dec('2aa', 16) == 682
    assert other2dec('20212202', 3) == 5015
    # test 2
    assert dec2other(682, 10) == '682'
    assert dec2other(682, 8) == '1252'
    assert dec2other(682, 16) == '2AA'
    assert dec2other(682, 2) == '1010101010'
    assert dec2other(10, 8) == '12'
    assert dec2other(10, 10) == '10'
    assert dec2other(10,16) == 'A'
    assert dec2other(5015, 9) == '6782'
    # test 3 dla zera
    assert other2dec('0', 2) == 0
    assert other2dec('0', 5) == 0
    assert other2dec('0', 8) == 0
    assert other2dec('0', 11) == 0
    assert other2dec('0', 16) == 0
    assert other2dec('0', 25) == 0

    print('KONIEC TESTOW')
    print("\n" * 1000)


if __name__ == '__main__':
    tests()
    main()
