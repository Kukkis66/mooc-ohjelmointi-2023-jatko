# TEE RATKAISUSI TÄHÄN:
class Auto:
    def __init__(self) -> None:
        self.__tankki = 0
        self.__km = 0

    def tankkaa(self):
        self.__tankki += 60

    def aja(self, km:int):
        if self.__tankki > 0:
            self.__tankki -= km
            self.__km += km

    def __str__(self) -> str:
        return f"Auto: ajettu{self.__km} km, bensaa {self.__tankki} litraa"
