# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        if self.__sentit < 10:
            return f"{self.__eurot}.0{self.__sentit} eur"
        else:
            return f"{self.__eurot}.{self.__sentit} eur"

    def __eq__(self, toinen):
        return self.__eurot + self.__sentit == toinen.__eurot + toinen.__sentit
    
    def __gt__(self, toinen):
        return self.__eurot + self.__sentit > toinen.__eurot + toinen.__sentit

    def __ne__(self, toinen):
        return self.__eurot + self.__sentit != toinen.__eurot + toinen.__sentit

    def __lt__(self, toinen):
        return self.__eurot + self.__sentit < toinen.__eurot + toinen.__sentit

    def __sub__(self, toinen):
        if toinen.__sentit > self.__sentit:
            self.__sentit += 100
            self.__eurot -= 1
        
        
        eurot = self.__eurot - toinen.__eurot
        sentit = self.__sentit - toinen.__sentit
        if eurot >= 0:
            if sentit < 10:
                return f"{eurot}.0{sentit} eur"
            else:
                return f"{eurot}.{sentit} eur"
        else:
            raise ValueError("ei voi olla miinuksella")
    
    def __add__(self, toinen):
        eurot = self.__eurot + toinen.__eurot
        sentit = self.__sentit + toinen.__sentit
        kulli = 100
        if sentit >= kulli:
            eurot += 1
            sentit = self.__sentit + toinen.__sentit - kulli
        if sentit < 10:
            return f"{eurot}.0{sentit} eur"
        else:
            return f"{eurot}.{sentit} eur"
    
if __name__ == "__main__":
    e1 = Raha(1, 0)
    e2 = Raha(2, 0)
    e3 = Raha(4, 10)
    
    print(e1 == e2)