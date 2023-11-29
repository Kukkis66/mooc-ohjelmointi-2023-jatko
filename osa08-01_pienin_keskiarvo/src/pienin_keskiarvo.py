# tee ratkaisu tänne
def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    arvot = ["tulos1", "tulos2","tulos3"]
    
    res1 = [henkilo1[i] for i in arvot if i in henkilo1]
    res2 = [henkilo2[i] for i in arvot if i in henkilo2]
    res3 = [henkilo3[i] for i in arvot if i in henkilo3]
    if sum(res1) < sum(res2) and sum(res1) < sum(res3):
        return henkilo1
    elif sum(res2) < sum(res3) and sum(res2) < sum(res1):
        return henkilo2
    elif sum(res3) < sum(res2) and sum(res3) < sum(res1):
        return henkilo3

            
        

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))