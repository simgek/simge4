# kullanıcı dışardan string olaraka sayı dizisi gönderecek  3 4 5 6 7 8 gibi

# geriye sayısal dizi olarak dndürünüz


def dizi(string):
    mylist = string.split()
    for n in range(len(mylist)):
        if mylist[n].count("."):
            mylist[n] = float(mylist[n])
        else:
            mylist[n] = int(mylist[n])
    return mylist
result = dizi("1 2 3 4 5 6 7.2 8")
print(result)
