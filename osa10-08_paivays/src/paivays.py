# TEE RATKAISUSI TÄHÄN:

class Paivays:
    def __init__(self, paiva:int, kuukausi: int, vuosi: int):
        self.paiva = paiva
        self.kuukausi = kuukausi
        self.vuosi = vuosi
        

    def __str__(self) -> str:
        return f"{self.paiva}.{self.kuukausi}.{self.vuosi}"

    def __eq__(self, a):
        return (self.paiva, self.kuukausi, self.vuosi) == (a.paiva, a.kuukausi, a.vuosi)

    def __gt__(self, a):
        return (self.vuosi , self.kuukausi , self.paiva) > (a.vuosi , a.kuukausi , a.paiva)
    
    def __lt__(self, a):
        
        return (self.vuosi, self.kuukausi,self.paiva) < (a.vuosi, a.kuukausi, a.paiva)

    def __ne__(self, a):
        return (self.paiva, self.kuukausi, self.vuosi) != (a.paiva, a.kuukausi, a.vuosi)


    def __add__(self, a):
        uusikuukausi = self.kuukausi
        uusivuosi = self.vuosi
        uusipaiva = self.paiva + a
        
        if uusipaiva >= 30:
            lisays = uusipaiva // 30
            uusikuukausi += lisays
            uusipaiva -= (30*lisays)
        
        if uusikuukausi >= 12:
            lisays = uusikuukausi // 12
            uusivuosi += lisays
            uusikuukausi -= (12*lisays)

        
        return Paivays(uusipaiva,uusikuukausi,uusivuosi)

    def __sub__(self, a):

        paivat1 = (self.vuosi - a.vuosi) * 360
        paivat2 = (self.kuukausi - a.kuukausi) * 30
        paivat3 = (self.paiva - a.paiva)
        if paivat1+paivat2+paivat3 < 0:
            return (paivat1+paivat2+paivat3) * -1
        else:
            return paivat1+paivat2+paivat3

if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(23, 5, 1999)
    p3 = Paivays(28, 5, 1985)



    
    
    print(p1 - p2)
    