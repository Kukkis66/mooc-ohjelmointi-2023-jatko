# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi: str, paino: int) -> None:
        self.nimi = nimi
        self.paino = paino

    def __str__(self) -> str:
        return f"{self.nimi} ({self.paino}kg) "

class Pakkaus:
    def __init__(self) -> None:
        self.pakkaus = []
    
    def lisaa_lahja(self, lahja: Lahja):
        self.pakkaus.append(lahja)

    def yhteispaino(self):
        yhteispaino = []
        for lahja in self.pakkaus:
            yhteispaino.append(lahja.paino)
        return sum(yhteispaino)

if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)

    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())

    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())