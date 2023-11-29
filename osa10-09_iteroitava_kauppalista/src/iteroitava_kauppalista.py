# TEE RATKAISUSI TÄHÄN:
class Kauppalista:
    def __init__(self):
        self.tuotteet = []

    def tuotteita(self):
        return len(self.tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.tuotteet[n - 1][1]

    # Iteraattorin alustusmetodi
    # Tässä tulee alustaa iteroinnissa käytettävä(t) muuttuja(t)
    def __iter__(self):
        self.n = 0
        # Metodi palauttaa viittauksen olioon itseensä, koska
        # iteraattori on toteutettu samassa luokassa
        return self

    # Metodi palauttaa seuraavan alkion
    # Jos ei ole enempää alkioita, heitetään tapahtuma
    # StopIteration
    def __next__(self):
        if self.n < len(self.tuotteet):
            # Poimitaan listasta nykyinen
            kirja = self.tuotteet[self.n]
            # Kasvatetaan laskuria yhdellä
            self.n += 1
            # ...ja palautetaan
            return kirja
        else:
            # Ei enempää kirjoja
            raise StopIteration
