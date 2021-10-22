def dec2bin():
    L1 = int(input("Podaj liczbe całkowitą L1: "))
    L2 = int(input("Podaj liczbe całkowitą L2: "))

    while L2 == 0:
        print("Nie będe mógł dzielić przez 0!")
        L2 = int(input("Podaj liczbe całkowitą L2: "))

    reszta = ""
    #L1//L2 - // - pełna liczba
    while True:
        print(f"L1 = {L1}, L2 = {L2}, L1//L2 = {L1//L2}, reszta {L1%L2}")
        reszta += f"{L1%L2}"
        if L1 // L2 == 0:
            break
        L1 = L1 // L2

    print(f"W systemie binarnym: {reszta[::-1]}")


if __name__ == '__main__':
    dec2bin()
