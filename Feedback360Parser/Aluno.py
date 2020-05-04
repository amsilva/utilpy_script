class Avaliado:

    def __init__(self, ra):
        self.ra = ra
        self.media = 0
        self.cont = 0
        self.total = 0

    def __str__(self):
        return self.ra

    def raGet(self):
        return self.ra

    def mediaGet(self):
        return self.media

    def contGet(self):
        return self.cont

    def avalia(self, comunic, compro, resul):
        self.cont = self.cont + 1
        self.total = self.total + int(comunic) + int(compro) + int(resul)
        self.media = self.total / (self.cont * 3)

