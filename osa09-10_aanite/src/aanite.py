# TEE RATKAISUSI TÄHÄN:
class Aanite:
    def __init__(self, pituus: int) -> None:
        self.pituus = 0
        if pituus > 0:
            self.__pituus = pituus
        else:
            raise ValueError("Ei voi olla negative")
    
    @property
    def pituus(self):
        return self.__pituus
    
    @pituus.setter
    def pituus(self, pituus: int):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("ei saa olla negatiivinen")
    
