"""
RO'YXATLAR BILAN ISHLASH

RO'YXATNI TARTIBLASH
Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin.
Buning uchun list uchun maxsus .sort() metodidan foydalaniladi.
"""

ismlar = ["Umar", "Nodir", "Ali", "Soli", "Akrom", "Dilshod", "Bahtiyor"]
ismlar.sort()  # Alifbo ketma-ketligi bo'yicha tartiblandi

# print(ismlar)

"""
Diqqat! Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling.
Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa, 
ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
"""

# Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritiladi

avtolar = ["BMW", "audi", "Nissan", "tayota", "tesla", "chevrolet"]
avtolar.sort(reverse=True)
# print(avtolar)

"""
.sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini
buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
"""

mevalar = ["Olma", "O'rik", "Behi", "Shaftoli", "Anjir", "Gilos"]

# print(sorted(mevalar))
# print(mevalar)

#   sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:

mevalar = ["Olma", "O'rik", "Behi", "Shaftoli", "Anjir", "Gilos"]

# print(sorted(mevalar, reverse=True))

#  SONLI RO'YHAT

sonlar = [10, 25, 65, 85, 978, 671, 37]

sonlar.sort()
print(sonlar)

sonlar.sort(reverse=True)
print(sonlar)

print(sorted(sonlar))
print(sorted(sonlar, reverse=True))

"""
RO'YXATNI AYLANTIRISH
Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. 
Buning uchun .reverse() metodidan foydalanamiz.
"""

avtolar = ["BMW", "audi", "Nissan", "tayota", "tesla", "chevrolet"]

avtolar.reverse()
print(avtolar)


"""
Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
"""

sonlar = [10, 25, 65, 85, 978, 671, 37]
mevalar = ["Olma", "O'rik", "Behi", "Shaftoli", "Anjir", "Gilos"]

print(len(sonlar))
print(len(mevalar))

"""
range() FUNKTSIYASI
Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin.
list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
"""

sonlar1 = list(range(1, 100))  # Diqqat! E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.

# print(sonlar1)

"""
Yuqoridagi misolda range(0,100) funktsiyasi 0 dan 99 gacha sonlar ketma-ketligini shakllantirdi, 
list(range(0,100)) esa bu ketma-ketlikni ro'yxatga aylantirdi.

range() yordamida qadamni ham berishimiz mumkin:
"""

juft_sonlar = list(range(0, 100, 2)) # 0 dan 100 gacha 2 qadam bilan
toq_sonlar = list(range(1, 100, 2))  # 1 dan 100 gacha 2 qadam bilan

# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

"""
SONLI RO'YXAT USTIDA SODDA AMALLAR

Pythonda ro'yxatlar ustida ba'zi sodda amallarni ham bajarish mumkin. 
Misol uchun ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, 
eng katta sonni topish uchun esa max() funktsiyasidan, 
sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:
"""

narxlar = [5_000, 23_000, 12_000, 9_000, 17_000, 42_000, 3_000, 7_000]

arzon_narhlar = min(narxlar)
qimmat_narxlar = max(narxlar)
umumiy_qiymat = sum(narxlar)

print(f"Arzon narxlar: {arzon_narhlar}\n Qimmat narxlar: {qimmat_narxlar}\n Umumiy qiymat: {umumiy_qiymat}")


"""
RO'YXATNI KESISH

Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin,
deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz,
buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
"""

cars = ['audi', 'bmw', 'nissan', 'tesla', 'chevrolet', 'ferrari', 'tayota', 'nexia']

print(cars[:3])  # 3 ta element ajratib olindi
print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)

print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi


"""
RO'YXATDAN NUSXA OLISH

Dastur davomida biror ro'yxatdan nusxa olish talab qilinishi mumkin. 
Buning uchun yuoqirdagi ka'bi ro'yxatni kesish usulidan foydalanamiz. 
Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
"""

sonlar2 = [1, 2, 3, 4, 5]  # sonlar2 ro'yxat yaratamiz
sonlar3 = sonlar2[:] # [:] ro'yhatni ko'chirib oladi

sonlar3.append(6)
sonlar3.append(7)

print("Asl royhat: ", sonlar2)
print("Nusxalangan ro'yxat: ", sonlar3)


"""
TUPLES - O'ZGARMAS RO'YXAT

Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. 
Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, 
dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda, 
Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
"""

tup_les = ('bir', 'ikki', 'uch')  # tuples()  ro'yxati

#  Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:

tup_les = ('bir', 'ikki', 'uch')

print(tup_les[0]) # birinchi element
print(tup_les[1])  # ikkinchi element
print(tup_les[2])  # uchunchi element

"""
Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida
List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi 
yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
"""

hafta_kunlari = ("Duyshanba", "Seyshanba", "Chorshanba", "Payshanba", "Juma")  # o'zgarmas ro'yxat
hafta_kunlari = list(hafta_kunlari) # o'zgarmas ro'yxatni listga o'zgartirildi

print(hafta_kunlari)

hafta_kunlari.append("Shanba")
hafta_kunlari.append("Yakshanba")

hafta_kunlari = tuple(hafta_kunlari) # listdan ozgarmas ro'yhatga o'tkazildi

print(hafta_kunlari)



