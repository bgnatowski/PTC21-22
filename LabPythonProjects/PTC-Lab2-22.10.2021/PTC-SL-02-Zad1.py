# STAŁE
NUMBER_ADDED_TO_REMINDER_FOR_ALPHABETIC_CHARS = 55
MIN_BASE_WITHOUT_ALPHABETIC_CHARS = 10
MIN_BASE = 2
MAX_BASE = 36
#####################


# @params dec2other:
# @param (string)number - liczba przeliczana w systemie 10
# @param (int)outputBase - podstawa wyjściowa
#
# @return (string)reminders - reszty w odwrotnej kolejności = liczba o podstawie wyjściowej
def dec2other(number, outputBase):
    number = int(number)  # rzutuje (string)liczbę na (int)liczbę
    reminders = []  # pusta tablica na reszty z dzielenia
    while number != 0:  # wykonuje algorytm dopóki liczba jest różna od 0
        reminder = number % outputBase  # dzieli modulo i zapisuje reszte z dzielenia
        if reminder >= MIN_BASE_WITHOUT_ALPHABETIC_CHARS:  # jeśli reszta z dzielenia jest >= 10
            reminders.append(chr(reminder + NUMBER_ADDED_TO_REMINDER_FOR_ALPHABETIC_CHARS))  # dodaje do tablicy reszt wartość litery
        else:
            reminders.append(str(reminder))  # w przeciwnym wypadku dodaje do tablicy reszte wprost ale rzutowaną na string
        print(f'{number} / {outputBase} = {number // outputBase} reszta {reminder}')
        number = number // outputBase  # dzieli liczbę przez podstawe i zapisuje wynik jako liczbę
    reminders.reverse()
    return "".join(reminders)


# @params getValue:
# @param (char)char - pojedynczy znak liczby
#
# @return (int)value - wartość znaku
def getValue(char):
    if char.isdigit():  # jeśli znak jest liczbą konwertuje wprost na wartość int
        value = int(char)
    elif 'a' <= char.lower() <= 'z':  # jeśli znak jest literą konwertuje kolejno A = 10, B = 11, C = 12,..., Z = 36
        value = ord(char.lower()) - ord('a') + 10
    return value


# @params getValuesOf:
# @param (string)number - liczba przeliczana
#
# @return (char[])values - tablica wartości poszczególnych znaków
def getValuesOf(number):
    values = []
    numberLen = len(number)

    for i in range(numberLen):
        char = number[i]  # pobiera i-ty znak z liczby
        charValue = getValue(char)  # zwraca wartość znaku
        values.append(charValue)  # dodaje wartość znaku do tablicy
    return values


# @params other2dec:
# @param (string)number - liczba przeliczana
# @param (int)inputBase - podstawa wejściowa
#
# @return (int)numberIn10 - przeliczona liczba z podstawy wejściowej na liczbę o podstawie 10
def other2dec(number, inputBase):
    ValuesOfNumberArray = getValuesOf(number)  # zwraca wartości każdego znaku w liczbie
    numberLen = len(number)  # długość liczby
    numberIn10 = 0

    # numberIn10 = a_(n-1)*p^(n-1)+a_(n-2)*p^(n-2)+...+ a_0*p^0
    for i in range(numberLen):
        numberLen -= 1  # słuzy jako wykładnik i jest z każdą iteracją zmniejszany o 1 do 0;
        char = number[i].upper()  # zmienia znak litery na dużą literę(potrzebne do printa)
        charValue = ValuesOfNumberArray[i]  # pobiera wartość znaku z tabicy wartości
        numberIn10 += charValue * (inputBase ** numberLen)  # dokonuje konwersji według wzoru
        print(f'{i}. znak to {char} ({charValue}*{inputBase}^{numberLen})')

    print(f'Liczba {number}({inputBase}) w sys 10 = {numberIn10}')
    print('Teraz nastąpi przeliczenie na liczbe na zadaną podstawie wyjściowa:')
    return numberIn10


# @params getOutputBase:
# @param (int)inputBase - podstawa liczby przeliczanej (potrzebna do sprawdzenia czy nie przeliczamy na te samą podstawę)
#
# @return (int)base - podstawa na którą będzie konwertowana liczba
def getOutputBase(inputBase):
    base = int(input(f'Podaj podstawę liczby wynikowej: (2-36) bez ({inputBase}): '))

    # warunek sprawdzający poprawność wpisanej podstawy wyjściowej
    while (MIN_BASE > base < MAX_BASE) or (base == inputBase):
        print('Błedna podstawa!')
        if base == inputBase:
            print(f'Po co przeliczać liczbę o podstawie ({inputBase}) na tą samą?')

        base = int(input(f'Podaj podstawę liczby wynikowej (2-36) bez ({inputBase}): '))

    return base


# @params isCorrectChar:
# @param (char)char - pojedynczy znak w liczbie (albo liczba, albo litera)
# @param (int)inputBase - podstawa liczby przeliczanej

# @return (boolean)isCorrect - czy znak jest poprawny dla podstawy
def isCorrectChar(char, inputBase):
    # sprawdza czy znak jest poprawny dla podstawy
    isCorrect = True

    if char.isdigit():
        # jeśli znak jest liczbą to sprawdź czy nie jest >= podstawie
        numberFromChar = int(char)
        if numberFromChar >= inputBase:
            isCorrect = False
            print(f'{numberFromChar} jest za duza dla podstawy: ({inputBase})')
    elif 'a' <= char.lower() <= 'z':
        # jeśli znak jest literą od "a do z" to zamień litere na jej wartość i sprawdz czy wartość nie jest >= podstawie
        valueOfChar = ord(char.lower()) - ord('a') + 10
        if valueOfChar >= inputBase:
            isCorrect = False
            print(f'{char} = {valueOfChar} jest za duzy dla podstawy: ({inputBase})')
    return isCorrect


# @params isCorrectForBase:
# @param (string)number - liczba o zadanej podstawie
# @param (int)inputBase - podstawa liczby przeliczanej
#
# @return (boolean)isCorrectForBase - czy liczba jest poprawnie zapisana dla podstawy
def isCorrectForBase(number, inputBase):
    # sprawdza czy podana liczba w systemie > 10 używa odpowienich dla siebie liter:
    # base(11) do A, base(12) do base(13) do C, base(14) do D .... base(36) do Z
    isCorrectForBase = True  # zwracana zmienna
    numberLen = len(number)  # ilość znaków w liczbie

    # pętla odpowiadająca za sprawdzenie każdego znaku w liczbie czy jest poprawny dla podstawy
    for i in range(numberLen):
        char = number[i]
        # instrukcja warunkowa wywołująca funkcję sprawdzająca poprawność
        # jeśli jakikolwiek znak jest niepoprawny pętla się przerywa i isCorrectForBase zwraca False
        if not isCorrectChar(char, inputBase):
            isCorrectForBase = False
            break
    return isCorrectForBase


# @params of getNumberInBase:
# @param (int)base - podstawa liczby przeliczanej
#
# @return (string)number - liczba w systemie o podstawie @param(base)
def getNumberInBase(base):
    while True:
        number = input(f'Podaj liczbe w systemie ({base}):')
        if isCorrectForBase(number, base):  # wywołuje funkcję sprawdzającą czy podany numer jest poprawnie zapisany dla podstawy
            return number
        else:
            continue


# @return (int)base - podstawa systemu liczby do przeliczenia
def getInputBase():
    base = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    while (MIN_BASE > base < MAX_BASE):  # podstawa systemu musi się zawierać [2;36]
        print('Błedna podstawa!')
        base = int(input('Podaj podstawę liczby do przeliczenia (2-36): '))
    return base


def main():
    while True:
        print('***Program do przeliczania liczby pomiędzy dwoma systemami liczbowymi***\n')

        inputBase = getInputBase()  # pyta użytkownika i pobiera podstawę systemu z którego bedzie przeliczana liczba
        inputNumber = getNumberInBase(inputBase)  # pyta użytkownika o liczbę o podanej wczesniej podstawie
        outputBase = getOutputBase(inputBase)  # pyta użytkownika o podstawę na jaką chce skonwertować liczbę

        numberIn10 = other2dec(inputNumber, inputBase)  # konwertuje liczbę o dowolnej podstawie na liczbę w systemie 10

        # if służący wyłapaniu liczby 0 (aby poprawnie wypisać wynik)
        if numberIn10 == 0:
            outputNumber = '0'
        else:
            outputNumber = dec2other(numberIn10, outputBase)  # konwertuje wczesniej przeliczoną liczbę na liczbę w zadanym systemie

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
    # test 4 dla poprawnosci znakow
    assert isCorrectForBase('A', 10) == False
    assert isCorrectForBase('A', 11) == True
    assert isCorrectForBase('A', 12) == True
    assert isCorrectForBase('abcdef', 16) == True
    assert isCorrectForBase('cab', 13) == True
    print('KONIEC TESTOW')
    print("\n" * 1000)


if __name__ == '__main__':
    tests()
    main()
