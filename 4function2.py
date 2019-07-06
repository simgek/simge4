# dışardan girilen değerin tek veya çift olma durumuna göre geriye değer dönen metot sayı çift ise -1 tek ise 1 sıfıra eşit ise 0 değerini teslim et


def a(sayi):
    result = 0
    if sayi == 0:
        return 0
    elif sayi % 2 == 0:
        return -1
    else:
        result = 1
    return result
result = a(int(input("lütfen bir sayı giriniz : ")))
print(result)

