# dışardan aldığı isim ve soyisime göre mail adresi oluşturan metot


def email(isim , soyisim = None):
    if soyisim is None:
       mail = "{}@hotmail.com".format(isim.lower())
    else:
        mail = "{}.{}@hotmail.com".format(isim.lower(),soyisim.lower())
    print(mail)
email(input("lütfen adınızı giriniz :"), input("lütfen soyadınızı giriniz : "))