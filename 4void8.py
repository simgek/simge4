# dışardan aldığınız değere göre kare çizenmetot

def dortgen(sayi):
    index = 0
    while index <= sayi:
        metin = ""
        for i in range(sayi + 1):
            metin += "X "
        print(metin)
        index += 1

dortgen(10)


def dortgen(sayi):
    index = 0
    while index <= sayi:
        print("X "* sayi)
        index += 1
dortgen(10)