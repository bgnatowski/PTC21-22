def zad3():
    tekstWiek = input("Podaj swój wiek: ")
    plec = input("Wprowadz płeć (m/k): ")

    if plec == "m":
        czyKobieta = False
    else:
        czyKobieta = True

    czyWszystkieSaLiczba = True
    for i in range(len(tekstWiek)):
        if not tekstWiek[i].isdigit():
            czyWszystkieSaLiczba = False

    if czyWszystkieSaLiczba and not czyKobieta:
        liczbaWiek = int(tekstWiek)
        ileDoEmerytury = 67-liczbaWiek

        if ileDoEmerytury == 0:
            print("Brawo osiągnąłeś wiek emerytalny!")
        elif (ileDoEmerytury > -10) and (ileDoEmerytury < 0):
            print(f"Jesteś już na emeryturze: {abs(ileDoEmerytury)} rok!")
        elif ileDoEmerytury <= -10:
            print(f"Jesteś już na emeryturze od: {abs(ileDoEmerytury)} lat!")
        else:
            print(f"Jesteś mężczyzną. Do wieku emerytalnego zostało Ci: {ileDoEmerytury}")
    elif czyWszystkieSaLiczba and czyKobieta:
        liczbaWiek = int(tekstWiek)
        ileDoEmerytury = 65-liczbaWiek

        if ileDoEmerytury == 0:
            print("Brawo osiągnęłaś wiek emerytalny!")
        elif (ileDoEmerytury > -10) and (ileDoEmerytury < 0):
            print(f"Jesteś już na emeryturze: {abs(ileDoEmerytury)} rok!")
        elif ileDoEmerytury <= -10:
            print(f"Jesteś już na emeryturze od: {abs(ileDoEmerytury)} lat!")
        else:
            print(f"Jesteś kobietą. Do wieku emerytalnego zostało Ci: {ileDoEmerytury}")
    else:
        print("Zmienna tekstWiek nie zawiera liczby dziesiętnej!")

    return 0


if __name__ == '__main__':
    zad3()
