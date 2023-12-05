KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:    
    def __init__(self, kapasiteetti = 0, kasvatuskoko = 0) -> None:
        self.alkioiden_lkm = 0

        # tarkista parametrit
        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise Exception("Kapasiteetin ja kasvatuskoon pitää olla positiivisia kokonaislukuja")
        
        if kapasiteetti == 0:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        
        if kasvatuskoko == 0:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)
        self.joukko = set()

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, x: int) -> list:
        return [0] * x

    def kuuluu(self, n: int) -> bool:
        return n in self.joukko

    def lisaa(self, n: int) -> bool:
        if self.kuuluu(n):
            return False
        else:
            self.joukko.add(n)
            return True

    def poista(self, n: int) -> bool:
        if self.kuuluu(n):
            self.joukko.remove(n)
            return True
        else:
            return False

    def mahtavuus(self):
        return len(self.joukko)

    def to_int_list(self):
        taulu = self._luo_lista(len(self.joukko))

        for i, n in enumerate(self.joukko):
            taulu[i] = n

            if (i + 1) % self.kapasiteetti == 0:
                taulu += self._luo_lista(self.kasvatuskoko)

        return taulu

    @staticmethod
    def yhdiste(a: "IntJoukko", b: "IntJoukko"):
        z = IntJoukko()

        # lisää a:n alkiot
        for n in a.joukko:
            z.lisaa(n)
        
        # lisää b:n alkiot
        for n in b.joukko:
            z.lisaa(n)

        return z

    @staticmethod
    def leikkaus(a: "IntJoukko", b: "IntJoukko"):
        z = IntJoukko()

        for x in a.joukko:
            for y in b.joukko:
                if x == y:
                    z.lisaa(y)

        return z

    @staticmethod
    def erotus(a: "IntJoukko", b: "IntJoukko"):
        z = IntJoukko()

        # lisää a:n alkiot
        for n in a.joukko:
            print(z.lisaa(n))

        # poista b:n alkiot
        for n in b.joukko:
            print(z.poista(n))

        return z

    def __str__(self):
        if len(self.joukko) == 0:
          return "{}"
        else:
          return str(self.joukko)
