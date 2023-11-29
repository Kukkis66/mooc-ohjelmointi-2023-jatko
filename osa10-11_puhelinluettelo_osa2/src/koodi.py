
# Tee ratkaisusi tähän:

class Henkilo:
    def __init__(self, nimi:str) -> None:
        self.nimis = nimi
        self.numerots = []
        self.osoites = None

    def lisaa_numero(self, numero:str):
        self.numerots.append(numero)

    def lisaa_osoite(self, osoite:str):
        self.osoites = osoite

    def nimi(self):
        return self.nimis
    
    def osoite(self):
            return self.osoites
    
    def numerot(self):
        if len(self.numerots) == 0:
            return self.numerots
        else:
            return self.numerots




        
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)

    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]
    
    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)

    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 nimen lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_tiedot(nimi)
        if numerot == None:
            print("numero ei tiedossa\nosoite ei tiedossa") 
            return
        elif len(numerot.numerot()) == 0:
            print(f"{numerot.nimi()}\nnumero ei tiedossa\n{numerot.osoite()}")
        elif numerot.osoite() == None:
            print(f"{numerot.nimi()}\n{numerot.numerot()[0:]}\nosoite ei tiedossa")
        else:
            print(f"{numerot.nimi()}\n{numerot.numerot()[0:]}\n{numerot.osoite()}")       

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
