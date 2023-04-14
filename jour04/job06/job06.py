liste=[1, 2, 3, 4, 5, 6]
def invertion():
    tmp=liste[0]
    liste[0]=liste[-1]
    liste[-1]=tmp
    print(liste)
invertion()
invertion()