# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    for i in matriisi:
        i.append(sum(i))
    


if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)