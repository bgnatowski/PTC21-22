def zad2():
    x1 = int(input("Podaj x1: "))
    x2 = int(input("Podaj x2: "))

    if x1 <= x2:
        for i in range(x1, x2+1):
            print(i)
    elif x1 > x2:
        for i in range(x1, x2-1, -1):
            print(i)
    print(f"|x1 - x2| = {abs(x1-x2)}")


if __name__ == '__main__':
    zad2()
