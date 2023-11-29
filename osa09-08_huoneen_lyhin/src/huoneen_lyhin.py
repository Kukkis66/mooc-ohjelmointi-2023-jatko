# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self) -> None:
        self.lista = []
        
    def lisaa(self, henkilo: Henkilo):
        self.lista.append(henkilo)
    
    def on_tyhja(self):
        if len(self.lista) > 0:
            return False
        else:
            return True
    
    def tulosta_tiedot(self):
        yhteispituus = []
        for henkilo in self.lista:
            yhteispituus.append(henkilo.pituus)
        print(f"Huoneessa on {len(self.lista)} henkilöä, yhteispituus on {sum(yhteispituus)} cm")
        for henkilo in self.lista:
            print(f"{henkilo.nimi} ({henkilo.pituus} cm)")

    def lyhin(self):
        if len(self.lista) > 0:
            lyhin = []
            nimet = []
            for henkilo in self.lista:
                lyhin.append(henkilo.pituus)
                nimet.append(henkilo.nimi)
            for henkilo in lyhin:
                index = min(lyhin)
            return self.lista[(lyhin.index(index))]
        else:
            return None

    def poista_lyhin(self):
        lyhin_henkilo = self.lyhin()
        for henkilo in self.lista:
            if henkilo.pituus == lyhin_henkilo.pituus:
                self.lista.remove(henkilo)
        return lyhin_henkilo


if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()