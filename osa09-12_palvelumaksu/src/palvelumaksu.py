# TEE RATKAISUSI TÄHÄN:
class Pankkitili:
    def __init__(self, tilinomistaja: str, tilinumero: str, saldo: float) -> None:
        self.__tilinomistaja = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo



    def __palvelumaksu(self):
        self.__saldo *= float(0.99)
    
    
    @property
    def saldo(self):
        return f"{self.__saldo}"
    
    
    def talleta(self,summa: float):
        if isinstance(summa, float):
            self.__saldo += summa
            self.__palvelumaksu()
            
    
    def nosta(self,summa: float):
        if isinstance(summa, float):
            if summa >= 0.0:
                self.__saldo = self.__saldo - float(summa)
                self.__palvelumaksu()
            
        
        
tili = Pankkitili("seppo", "12345-6789", 1000)

print(tili.saldo)
tili.talleta("seppo")
print(tili.saldo)
