# tee ratkaisusi tänne

class Opintorekisteri:
    def __init__(self) -> None:
        self.__rekisteri = {}

    def lisaa_suoritus(self, kurssi: str, arvosana: int, pisteet: int):
        if not kurssi in self.__rekisteri:
            self.__rekisteri[kurssi] = {}
            self.__rekisteri[kurssi]["arvosana"] = arvosana
        if arvosana >= self.__rekisteri[kurssi]["arvosana"]:
            self.__rekisteri[kurssi]["arvosana"] = arvosana
        
        self.__rekisteri[kurssi]["pisteet"] = pisteet


    def hae_suoritus(self, kurssi: str):
        if not kurssi in self.__rekisteri:
            return None
        return self.__rekisteri[kurssi]

    def tilastot(self):
        return self.__rekisteri






class OpintorekisteriSovellus:
    def __init__(self):
        self.__opintorekisteri = Opintorekisteri()


    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
    
    def suorituksen_lisays(self):
        kurssi = input("kurssin nimi: ")
        numero = int(input("kurssin numero: "))
        if numero > 5:
            return
        pisteet = int(input("kurssin opintopisteet: "))
        self.__opintorekisteri.lisaa_suoritus(kurssi, numero, pisteet)

    def suorituksen_haku(self):
        kurssi = input("anna kurssin nimi")
        haku = self.__opintorekisteri.hae_suoritus(kurssi)
        if haku == None:
            print("ei suoritusta")
            return
        print(f"{kurssi} ({haku['pisteet']} op) arvosana {haku['arvosana']}")

    def tilastojen_haku(self):
        tilasto = self.__opintorekisteri.tilastot()
        kurssit = []
        arvosanat = []
        opintopisteet = []
        for kurssi, pisteet in tilasto.items():
            kurssit.append(kurssi)
            arvosanat.append(int(pisteet["arvosana"]))
            opintopisteet.append(int(pisteet["pisteet"]))
        print(f"suorituksia {len(kurssit)} kurssilta, yhteensä {sum(opintopisteet)} opintopistettä")
        print(f"keskiarvo {round(sum(arvosanat)/len(arvosanat), 1)}")
        print(f"arvosanajakauma")
        seppo = 6
        while seppo > 1:
            seppo -= 1
            muuttuja = "x" * arvosanat.count(seppo)
            print(f"{seppo}: {muuttuja}")



    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.suorituksen_haku()
            elif komento == "3":
                self.tilastojen_haku()
            else:
                self.ohje()

perse = OpintorekisteriSovellus()
perse.suorita()