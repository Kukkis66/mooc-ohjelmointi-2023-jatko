# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.lista = []
    
    
    def lisaa_luku(self, luku:int):
        self.lista.append(luku)
        self.lukuja += 1

    def lukujen_maara(self):
        return self.lukuja

    def summa(self):
        return sum(self.lista)

    def keskiarvo(self):
        try:
            if len(self.lista) > 0:
                return sum(self.lista)/len(self.lista)
        except:
            pass

# tilasto = Lukutilasto()
# while True:
#     a = int(input("Anna lukuja:"))
#     tilasto.lisaa_luku(a)
#     if a < 0:
#         print("Summa: ",tilasto.summa())
#         print("Keskiarvo: ",tilasto.keskiarvo())
#         break

tilasto = Lukutilasto()
tilasto1 = Lukutilasto()
tilasto2 = Lukutilasto()

while True:
    a = int(input("Anna lukuja:"))
    
    if a >= 0:
        tilasto.lisaa_luku(a)
        if a % 2 == 0:
            tilasto1.lisaa_luku(a)
        elif a % 2 == 1:
            tilasto2.lisaa_luku(a)
    elif a < 0:
        print("Summa:",tilasto.summa())
        print("Keskiarvo:",tilasto.keskiarvo())
        print("Parillisten summa:",tilasto1.summa())
        print("Parittomien summa:",tilasto2.summa())
        break
