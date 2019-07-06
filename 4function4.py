# dışardan bir sayısal dizisinin parametre olarak alan bir metot yazın metot
# parametredki dizide yer alan elemanların toplamanın karekökünü döndürüsün

import math # import anahtar kelimesi içerde var olan herhangi bir kütüphaneyi teslim etmek için kullanırız
def karekok(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return math.sqrt(toplam)


sonuc = karekok([1,2,3,4,5,6])
print("işlem sonucu : ", sonuc)