from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self, tekoaly = Tekoaly()):
        self.tuomari = Tuomari()
        self.tekoaly = tekoaly

    def _toisen_siirto(self):
        return self.tekoaly.anna_siirto()
