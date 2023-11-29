# TEE RATKAISUSI TÄHÄN:
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")


class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        else:
            pass
        
class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        vokaalit = ["a", "e", "i", "o", "u", "y", "ä", "ö"]
        pituus1 = []
        pituus2 = []
        
        for i in list(pelaaja1_sana):
            if i in vokaalit:
                pituus1.append(i)
        
        for i in list(pelaaja2_sana):
            if i in vokaalit:
                pituus2.append(i)
        
        if len(pituus1) > len(pituus2):
            return 1
        elif len(pituus1) < len(pituus2):
            return 2
        else:
            pass

class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)



    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        sanat = ["kivi", "paperi", "sakset"]
        
        if pelaaja1_sana not in sanat and pelaaja2_sana in sanat:
            return 2
        elif pelaaja2_sana not in sanat and pelaaja1_sana in sanat:
            return 1
            
        elif pelaaja1_sana == "kivi" and pelaaja2_sana == "sakset":
            return 1
        elif pelaaja2_sana == "kivi" and pelaaja1_sana == "sakset":
            return 2

        elif pelaaja1_sana == "paperi" and pelaaja2_sana == "sakset":
            return 2
        elif pelaaja2_sana == "paperi" and pelaaja1_sana == "sakset":
            return 1

        elif pelaaja1_sana == "kivi" and pelaaja2_sana == "paperi":
            return 2
        elif pelaaja2_sana == "kivi" and pelaaja1_sana == "paperi":
            return 1
        else:
            pass



    


