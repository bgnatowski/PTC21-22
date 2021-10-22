def zad5():
    slowo = input("Podaj jakieś słowo/znak/tekst: ")
    zmienSlowoNaASCII(slowo)


def zmienSlowoNaASCII(slowo):
    kodAsciiZera = ord("0")
    wynik = ""
    for i in range(len(slowo)):
        znak = slowo[i]
        wynik += f"{znak} {ord(znak)-55}\n" # przy robieniu konwersji zadeklaruj zmienna STAŁĄ
    print(wynik)

if __name__ == '__main__':
    zad5()
