# TEE RATKAISUSI TÄHÄN:
class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    def pinta_ala(self):
        return self.leveys * self.korkeus


class Nelio(Suorakulmio):
    def __init__(self, leveys: int, korkeus=1):
        super().__init__(leveys, korkeus)

    def __str__(self):
        korkeus = self.leveys
        return f"neliö {self.leveys}x{korkeus}"

    def pinta_ala(self):
        korkeus = self.leveys
        return self.leveys * korkeus
        

