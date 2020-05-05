class Avaliado:

    def __init__(self, ra):
        self.ra = ra
        self.cont = 0
        self.totalcomu = 0
        self.totalcomp = 0
        self.totalresu = 0

    def __str__(self):
        return self.ra

    def raGet(self):
        return self.ra

    def mediaGet(self):
        return self.totalGet() / (self.cont * 3)

    def totalGet(self):
        return self.totalcomu + self.totalcomp + self.totalresu

    def mediaCompGet(self):
        return self.totalcomp / self.cont

    def mediaComuGet(self):
        return self.totalcomu / self.cont

    def mediaResuGet(self):
        return self.totalresu / self.cont

    def contGet(self):
        return self.cont

    def avalia(self, comu, comp, resu):
        self.cont = self.cont + 1
        self.totalcomu = self.totalcomu + int(comu)
        self.totalcomp = self.totalcomp + int(comp)
        self.totalresu = self.totalresu + int(resu)

