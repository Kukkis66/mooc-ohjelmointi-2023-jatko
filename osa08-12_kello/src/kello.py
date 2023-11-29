
# Tee ratkaisusi tähän:
class Kello:
    def __init__(self, tunnit: int, minuutit:int, sekunnit: int):
        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    def tick(self):
        try:
            self.sekunnit += 1
            if self.sekunnit == 60:
                self.sekunnit = 0
                self.minuutit +=1
            if self.minuutit == 60:
                self.minuutit = 0
                self.tunnit += 1
            if self.tunnit == 24:
                self.tunnit = 0
        except:
            self.sekunnit == 0
            return self
    
    def aseta(self, tunnit=00, minuutit=00, sekunnit=00):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit



    def __str__(self):
        if self.minuutit < 10:
            minuutit = f"{0}{self.minuutit}"
        else:
            minuutit = self.minuutit
        if self.sekunnit < 10:
            sekunnit = f"{0}{self.sekunnit}"
        else:
            sekunnit = self.sekunnit
        if self.tunnit < 10:
            tunnit = f"{0}{self.tunnit}"
        else:
            tunnit = self.tunnit
        
        return f"{tunnit}:{minuutit}:{sekunnit}"

if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)