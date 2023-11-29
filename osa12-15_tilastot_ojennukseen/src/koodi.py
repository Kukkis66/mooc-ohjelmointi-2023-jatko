# tee ratkaisusi tänne
import json


class Tiedostonkasittelija:
    def __init__(self) -> None:
        pass
    
    def tiedosto(self, file):
        

        with open(file) as tiedosto:
            data = tiedosto.read()
            tiedot = json.loads(data)
            return tiedot
            
    





class TilastotSovellus:
    def __init__(self, tiedosto) -> None:
        self.tiedot = Tiedostonkasittelija.tiedosto(self,tiedosto)
        self.tiedostonimi = tiedosto

    def ohje(self):
        print("komennot:")
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")
    
    def tietoja(self):
        print("tiedosto:",self.tiedostonimi)
        print("luettiin",len(self.tiedot),"pelaajan tiedot")

    def nimilaatikko(self, nimi):
        vali = " "
        stringi = nimi
        while len(stringi) < 21:
            stringi += vali
        return stringi
    
    def valit(self, numero): #tämä lisää välejä pelaajalistan printtaukseen
        
        if numero > 100:
            return f""
        elif numero >= 10:
            return f" "
        else:
            return f"  "
    
    def hae_pelaaja(self, nimi: str):
        for i in self.tiedot:
            if i["name"] == nimi:
                
                print(f"{self.nimilaatikko(i['name'])}{i['team']} {self.valit(i['goals'])}{i['goals']} +{self.valit(i['assists'])}{i['assists']} = {self.valit((i['goals'] + i['assists']))}{(i['goals'] + i['assists'])}")

    def joukkueet(self):
        joukkuelista = []
        for i in self.tiedot:
            if i["team"] not in joukkuelista:
                joukkuelista.append(i["team"])
        joukkuelista.sort()
        for i in joukkuelista:
            print(i)

    def joukkueen_pelaajat(self, joukkue):
        pelaajat = {}
        for i in self.tiedot:
            if i["team"] == joukkue:
                pelaajat[i["name"]] = (i["goals"] + i["assists"])
        pelaajat = dict(sorted(pelaajat.items(), key=lambda item: item[1], reverse=True))
        pelaajalista = [key for key in pelaajat]

        for i in pelaajalista:
            self.hae_pelaaja(i)
    
    def maan_pelaajat(self, maa):
        pelaajat = {}
        for i in self.tiedot:
            if i["nationality"] == maa:
                pelaajat[i["name"]] = (i["goals"] + i["assists"])
        pelaajat = dict(sorted(pelaajat.items(), key=lambda item: item[1], reverse=True))
        pelaajalista = [key for key in pelaajat]

        for i in pelaajalista:
            self.hae_pelaaja(i)



    def maat(self):
        maalista = []
        for i in self.tiedot:
            if i["nationality"] not in maalista:
                maalista.append(i["nationality"])
        maalista.sort()
        for i in maalista:
            print(i)

    def eniten_pisteita(self, monta: int):
        pelaajat = {}
        for i in self.tiedot:
            pelaajat[i["name"]] = (i["goals"] + i["assists"])
        pelaajat = dict(sorted(pelaajat.items(), key=lambda item: item[1], reverse=True))
        pelaajalista = [key for key in pelaajat]
        x = 0
        while x < monta:
            self.hae_pelaaja(pelaajalista[x])
            x += 1


    def eniten_maaleja(self, monta: int):
        pelaajat = {}
        for i in self.tiedot:
            pelaajat[i["name"]] = {"goals" : i["goals"], "games" : i["games"]}
        pelaajalista = list(sorted(pelaajat, key=lambda item: (pelaajat[item]["goals"], -pelaajat[item]["games"]),reverse=True))
        x = 0
        while x < monta:
            self.hae_pelaaja(pelaajalista[x])
            x += 1
            




    def ohjelma(self):
        self.tietoja()
        print("")
        self.ohje()
        
        while True:
            print("")
            komento = input("komento:")
            if komento == "0":
                break
            elif komento == "1":
                nimi = input("nimi: ")
                self.hae_pelaaja(nimi)
            elif komento == "2":
                self.joukkueet()
            elif komento == "3":
                self.maat()
            elif komento == "4":
                joukkue = input("joukkue:")
                print("")
                self.joukkueen_pelaajat(joukkue)
            elif komento == "5":
                maa = input("maa:")
                print("")
                self.maan_pelaajat(maa)
            elif komento == "6":
                monta = int(input("kuinka monta:"))
                self.eniten_pisteita(monta)
            elif komento == "7":
                maaleja = int(input("kuinka monta:"))
                self.eniten_maaleja(maaleja)



filu = input()
perse = TilastotSovellus(filu)
perse.ohjelma()