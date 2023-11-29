# TEE RATKAISUSI TÄHÄN:
class Havaintoasema:
    def __init__(self, nimi: str) -> None:
        self.__nimi = nimi
        self.__lista = []

    def lisaa_havainto(self, havainto:str):
        self.__lista.append(havainto)

    def viimeisin_havainto(self):
        if len(self.__lista) > 0:
            return self.__lista[-1]
        else:
            return f""

    def havaintojen_maara(self):
        return len(self.__lista)

    def __str__(self) -> str:
        return f"{self.__nimi}, {len(self.__lista)} havaintoa"

if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    print(asema)
    asema.lisaa_havainto("Aurinkoista")
    print(asema)
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)
