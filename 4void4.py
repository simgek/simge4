# 1 ile 1000 arasındaki yer alan sayıların birbiryile toplamını yazınız


def hesap():
    toplam = 0
    for sayi in range (1,1001):
        toplam += sayi
    print(toplam)
hesap()

