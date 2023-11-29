# Tee ratkaisusi tähän:
class Tavara:
    def __init__(self, nimi: str, paino: int) -> None:
        self.tavaran_paino = paino
        self.tavaran_nimi = nimi

    def paino(self):
        return self.tavaran_paino

    def nimi(self):
        return self.tavaran_nimi

    def __str__(self) -> str:
        return f"{self.tavaran_nimi} ({self.tavaran_paino} kg)"

class Matkalaukku:
    def __init__(self, maksimipaino: int) -> None:
        self.maksimipaino = maksimipaino
        self.tavarat = []
    
    def lisaa_tavara(self, tavara):
        maksimipaino = self.maksimipaino
        if tavara.tavaran_paino <= maksimipaino:
            self.tavarat.append(tavara)
            self.maksimipaino -= tavara.tavaran_paino

    def tulosta_tavarat(self):
        for i in self.tavarat:
            value = i
            print(value)

    def paino(self):
        yhteispaino = []
        for i in self.tavarat:
            yhteispaino.append(i.tavaran_paino)
        return sum(yhteispaino)

    def raskain_tavara(self):
        paino = []
        for i in self.tavarat:
            paino.append(i.tavaran_paino)
        index = max(paino)
        return self.tavarat[(paino.index(index))]


    def __str__(self) -> str:
        yhteispaino = []
        for i in self.tavarat:
            yhteispaino.append(i.tavaran_paino)
        if len(self.tavarat) == 1:
            return f"{len(self.tavarat)} tavara ({sum(yhteispaino)} kg)"
        else:
            return f"{len(self.tavarat)} tavaraa ({sum(yhteispaino)} kg)"


class Lastiruuma:
    def __init__(self, maksimipaino: int) -> None:
        self.maksimipaino = maksimipaino
        self.lastiruuma = []

    def lisaa_matkalaukku(self, matkalaukku):
        maksimipaino = self.maksimipaino
        if matkalaukku.paino() <= maksimipaino:
            self.lastiruuma.append(matkalaukku)
    
    def tulosta_tavarat(self):
        tuloste = []
        for i in self.lastiruuma:
            tuloste.append(i.tulosta_tavarat())
        
        for i in tuloste:
            return i
                

    def __str__(self) -> str:
        yhteispaino = []
        for i in self.lastiruuma:
            yhteispaino.append(i.paino())
        if len(self.lastiruuma) == 1:
            return f"{len(self.lastiruuma)} matkalaukku, tilaa {self.maksimipaino - sum(yhteispaino)} kg"
        else:
            return f"{len(self.lastiruuma)} matkalaukkua, tilaa {self.maksimipaino - sum(yhteispaino)} kg"


        

if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()