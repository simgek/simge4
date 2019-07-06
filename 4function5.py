#dışardan dilediğin kadar sayı gir
#ve her sayı girdikten sonra sayı girmeye devam edip etmeyeceği sorulacak
#kullanıcı y veya Y tuşuna basarsa yeni bir sayı girmesi istenecek
# kullanıcı harici bir tuşa basarsa içeriye aldığı sayılar içerisindeki
# tek sayı ise içerisinde yer alan en büyük ve en küçük sayısının birbirine olan farkını geriye dçnecek


def fark():
    go_on = "y"
    tek = []
    while go_on == "y" or go_on == "Y":
        number = float(input("lütfen sayı girin : "))
        if number % 2 != 0:
            tek.append(number);
        go_on =input("yeni bir sayı eklemek istiyor musunuz (Y\\N)")

    return max(tek) - min(tek)
sonuc = fark()
print("işlem sonucu :",sonuc)