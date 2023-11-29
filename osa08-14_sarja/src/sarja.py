# Tee ratkaisusi tähän:

class Sarja:
    def __init__(self, nimi: str, seasons: int, genret: list):
        self.nimi = nimi
        self.seasons = seasons
        self.genret = genret
        self.arvosanat = []
        self.arvostelut = 0
        # if self.arvostelut > 0:
        #     self.arvostelu = sum(self.arvosanat)/len(self.arvosanat)
        #self.arvostelu = sum(self.arvosanat)/len(self.arvosanat)

    def arvostele(self, arvosana: int):
        self.arvosana = arvosana
        
        if self.arvosana > 0:
            if self.arvosana <= 5:
                self.arvostelut += 1
                self.arvosanat.append(self.arvosana)
        if self.arvostelut > 0:
            self.arvostelu = sum(self.arvosanat)/len(self.arvosanat)
            
        

    def __str__(self):
        genret = ", ".join(self.genret)
        if self.arvostelut > 0:
            arvostelu = sum(self.arvosanat)/len(self.arvosanat)
            return f"{self.nimi} ({self.seasons} esityskautta)\ngenret: {genret}\narvosteluja {self.arvostelut}, keskiarvo {arvostelu:.1f} pistettä"
        else:
            return f"{self.nimi} ({self.seasons} esityskautta)\ngenret: {genret}\nei arvosteluja"




def arvosana_vahintaan(arvosana: float, sarjat: list):
        n = 0
        while sarjat[n]:
            if arvosana < sarjat[n].arvostelu:
                sarjat.pop(n)
                if n == len(sarjat):
                    break
                n += 1
                return sarjat
        
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)

s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)

s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)

sarjat = [s1, s2, s3]

print("arvosana vähintään 4.5:")
for sarja in arvosana_vahintaan(4.5, sarjat):
    print(sarja.nimi)

# print("genre Comedy:")
# for sarja in sisaltaa_genren("Comedy", sarjat):
#     print(sarja.nimi)