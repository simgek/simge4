# dışardan alınan metin içerisindeki sesli harf ve sessiz harflerin adetini yazınız

def seslisessiz(string):
    sesli = ["a","e","ı","i","o","ö","u","ü"]
    liste = list(string)
    seslic = 0
    sessizc = 0
    for i in liste:
        if i in sesli:
            seslic += 1
        else:
            sessizc += 1
    print("toplam sesli harf sayısı : {}\ntoplam sessiz harf sayısı : {}".format(seslic,sessizc))

seslisessiz("simgekarademir")


