# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        try:
            self.sekunnit += 1
            if self.sekunnit == 60:
                self.sekunnit = 0
                self.minuutit +=1
            if self.minuutit == 60:
                self.minuutit = 0
        except:
            self.sekunnit == 0
            return self

    def __str__(self):
        if self.minuutit < 10 and self.sekunnit < 10:
            return f"{0}{self.minuutit}:{0}{self.sekunnit}"
        elif self.sekunnit < 10:
            return f"{self.minuutit}:{0}{self.sekunnit}"
        elif self.minuutit < 10:
            return f"{0}{self.minuutit}:{self.sekunnit}"
        else:
            return f"{self.minuutit}:{self.sekunnit}"

if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3601):
        print(kello)
        kello.tick()