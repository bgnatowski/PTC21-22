#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division


def main(args):
    reszty = []
    liczba = int(input("Podaj liczbe(dec): "))
    podstawa = int(input("Podaj podstawe: "))

    while liczba > 0:
        reszta = liczba % podstawa
        reszty.append(reszta)
        liczba = liczba // podstawa

    reszty.reverse()
    print(reszty)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
