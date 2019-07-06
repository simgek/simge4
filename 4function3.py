# dışardan girilen ilk kelimenin ilk iki harfi büyük
# geri kalanını küçükyazın
#ikinci kelimenin içerisinde geçen tüm alrı e ye çevirin
# ve sonuna @hotmail.com ekleyerek geri döndürün


def a(k1 , k2):
    k1_ = (k1[0]+k1[1]).upper() + str(k1)[2:].lower()
    k2_ = k2.replace("a","e")
    return "{}.{}@hotmail.com".format(k1_,k2_)


mail = a("simge","karademir")
print("kullanıcının mail adresi : ",mail)
