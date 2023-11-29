# TEE RATKAISUSI TÄHÄN:
class ListaApuri:
    def __init__(self) -> None:
        pass

    
    @classmethod
    def suurin_frekvenssi(self,lista: list):
        vastaus = max(set(lista), key= lista.count)
        return vastaus
    
    
    @classmethod   
    def tuplia(self,lista: list):
        kukka = []
        for i in range(len(lista)):
            if lista.count(i) >= 2:
                kukka.append(i)
        return len(kukka)

            


        

if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))