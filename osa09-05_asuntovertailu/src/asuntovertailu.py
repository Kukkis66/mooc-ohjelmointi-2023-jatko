# TEE RATKAISUSI TÄHÄN:

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    def suurempi(self, verrattava):
        if self.nelioita > verrattava.nelioita:
            return True
        else:
            return False

    def hintaero(self, verrattava):
        hinta_self = self.neliohinta * self.nelioita
        hinta = verrattava.neliohinta * verrattava.nelioita
        if hinta_self > hinta:
            return hinta_self - hinta
        elif hinta_self < hinta:
            return hinta - hinta_self

    def kalliimpi(self, verrattava):
        hinta_self = self.neliohinta * self.nelioita
        hinta = verrattava.neliohinta * verrattava.nelioita
        if hinta_self > hinta:
            return True
        elif hinta_self < hinta:
            return False



if __name__ == "__main__":
    eira_yksio = Asunto(1, 16, 5500)
    kallio_kaksio = Asunto(2, 38, 4200)
    jakomaki_kolmio = Asunto(3, 78, 2500)

    print(eira_yksio.hintaero(kallio_kaksio))
    print(jakomaki_kolmio.hintaero(kallio_kaksio))