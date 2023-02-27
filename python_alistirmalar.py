###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)


c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]

type(l)

d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")

type(t)

s = {"Python", "Machine Learning", "Data Science","Python"}

type(s)


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper()

text = "The goal is to turn data into information, and information into insight."
text = text.replace(",", "").replace(".", "")

text = "The goal is to turn data into information, and information into insight."
text = text.split(" ")

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.
lst = ["D","A","T","A","S","C","I","E","N","C","E"]
lst.pop(8)

# Adım 5: Yeni bir eleman ekleyin.

lst.append("K")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8,"N")

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

yeni_dict = {'Christian': ["America",18],
        'Daisy':["England",13],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

dict.update(yeni_dict)
# dict.update({'Daisy': ['England', 13]})


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = "[Turkey,24]"
dict

# Adım 5: Antonio'yu dictionary'den siliniz.
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}
dict.pop("Antonio")



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonksiyon yazınız.
###############################################


l = [2,13,18,93,22]

cift= []

tek=[]

def func(l):
    for i in l:
    if i % 2 ==0:
        cift.append(i)
    else:
        tek.append(i)
    return cift, tek

func(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


def universite(ogrenciler):
    for x,student in enumerate(ogrenciler):
        if x<3:
            print("Mühendislik Fakültesi " + str(x+1) + ". öğrenci: " + student)
        else:
            print("Tıp Fakültesi " + str(x-2) + ". öğrenci: " + student)

universite(ogrenciler)

#başka çözüm1
for index, x in enumerate(ogrenciler):
    if index == 0:
        print(f"Mühendislik Fakültesi {index +1 }. öğrenci: {x}")
    if index == 1:
        print(f"Mühendislik Fakültesi {index + 1}. öğrenci: {x}")
    if index == 2:
        print(f"Mühendislik Fakültesi {index + 1}. öğrenci: {x}")
    if index == 3:
        print(f"Tıp Fakültesi {index - 2}. öğrenci: {x}")
    if index == 4:
        print(f"Tıp Fakültesi {index - 3}. öğrenci: {x}")
    if index == 5:
        print(f"Tıp Fakültesi {index - 4}. öğrenci: {x}")

#başka çözüm2

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler):
    if index < 3:
        print("Mühendislik Fakültesi {}. öğrenci: {}".format(index+1, ogrenci))
    else:
        print("Tıp Fakültesi {}. öğrenci: {}".format(index-2, ogrenci))

#enumerate: indexle beraber ve ona bağlı ali veli ayşe ile yani, hem sırası hem değerle birlikte işlem yaptırmak istiyorsak



###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu, kredi, kontenjan))
#başka çözüm1
for ders_kodu, kredi, kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#başka çözüm2
ders_bilgisi = list(zip(kredi, ders_kodu, kontenjan))
for ders in ders_bilgisi:
    print("Kredisi ", ders[0], " olan ", ders[1], " kodlu dersin kontenjanı ", ders[2], " kişidir")
###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını, eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def fonk(kume1, kume2):
if kume1.issuperset(kume2) ==True:
    return(kume1.intersection(kume2))
else:
   return(kume2.difference(kume1))

fonk(kume1, kume2)

#başka çözüm1

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume_kapsama(kume1,kume2):
    if kume1.issuperset(kume2) == True:
        print("Kesisim: ", kume1.intersection(kume2))
    else:
        print("Fark: ", kume2.difference(kume1))

kume_kapsama(kume1,kume2)

#başka çözüm2
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def fark_set(kume1, kume2):
        if kume1.issuperset(kume2):
            print(kume1.intersection(kume2))
        else:
            print(kume2.difference(kume1))

fark_set(kume1, kume2)

#başka çözüm3
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])
def check(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

check(kume1, kume2)
check(kume2, kume1)