import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)

    joukko2 = IntJoukko()

    joukko2.lisaa(1)
    joukko2.lisaa(2)

    print(joukko.to_int_list())
    print()
    print(IntJoukko.erotus(joukko, joukko2))


if __name__ == "__main__":
    main()
