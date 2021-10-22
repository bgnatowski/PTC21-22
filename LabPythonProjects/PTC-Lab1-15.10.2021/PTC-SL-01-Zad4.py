def zad4():
    L1 = int(input("Podaj liczbe całkowitą L1: "))
    L2 = int(input("Podaj liczbe całkowitą L2: "))

    while L2 == 0:
        print("Nie będe mógł dzielić przez 0!")
        L2 = int(input("Podaj liczbe całkowitą L2: "))

    #L1//L2 - // - pełna liczba
    while True:
        print(f"L1 = {L1}, L2 = {L2}, L1//L2 = {L1//L2}, reszta {L1%L2}")
        if L1 // L2 == 0:
            break
        L1 = L1 // L2

    # print(f"L1/L2 = {L1/L2}\n L1%L2 = {L1%L2}")
    # modulo = L1%L2
    # while modulo != 0:
    #     print(f"{L1} {L2}")
    #     modulo = L1%L2
    #     iloraz = L1/L2
    #     print(f"L1/L2 = {iloraz} L1%L2 = {modulo}")
    #     L1 -= 1

    # while L1/L2 > 0:
    #     modulo = L1 % L2
    #     iloraz = L1 / L2
    #
    #     print(f"L1/L2 = {iloraz} L1%L2 = {modulo}")
    #
    #     L1 = iloraz
    #     if L2 == 1:
    #         break


if __name__ == '__main__':
    zad4()
