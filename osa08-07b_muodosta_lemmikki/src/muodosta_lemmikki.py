# Tee ratkaisusi tähän:
class Lemmikki:

    def __init__(self, nimi: str, laji: str, syntymavuosi: int) -> None:
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi





def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):
    return Lemmikki(nimi, laji, syntymavuosi)
    


if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)