"""
STRING (MATN) VA UNICODE

String - bu dasturlashda ishlatiladigan ma'lumot turi bo'lib, u raqamlarni emas,
balki matnni ifodalash uchun ishlatiladi. Satr - bu belgilar ketma-ketligi bo'lib,
unda harflar, raqamlar, belgilar va hatto bo'sh joy bo'lishi mumkin. 
U satr sifatida tan olinishi uchun qo'shtirnoq ichiga olinishi kerak.

Unicode - bu dunyodagi ko'pgina kompyuterlar uchun standart belgili kodlash.
Bu matn, jumladan, harflar, belgilar, emoji va hatto boshqaruv belgilarining operatsion tizim 
yoki dasturiy ta'minotdan qat'i nazar, turli qurilmalar, platformalar va raqamli hujjatlarda bir
xil ko'rinishini ta'minlaydi. Bu internet va hisoblash sanoatining muhim qismidir va usiz internet
ancha tartibsiz va undan foydalanish qiyinroq bo'lar edi.
"""

string1 = 'Давлатлар'  # string (matn) "" qo'shtirnoq yoki '' birtirnoq ichida yozzilishi kerak.
string2 = "Shaharlar"  


"""
Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan iborat bo'lishi mumkin 
(jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli emoji-smayliklar) 
"""

matn1 = "Men 🚗 sotib oldim."
matn2 = "Kirish mumkin emas 🚫"

# print(matn1)
# print(matn2)

#  String ustida amallar. Matinni qo'shish operatori +


poytaxt = "Toshkent"
print("O'zbekiston poytaxti " + poytaxt)

ism = "Falonchi"
familya = "Falonchiev"

print(ism + familya) # bunday holatda ism familya qo'shilib qoladi buni oldini olish uchun bo'sh joy qo'yiladi.
print(ism + " " + familya) # ✅

# ikki va undan ko'p matnlarni qo'shishda f string usulidan foydalaniladi. f"{matn1} {matn2}""

bahor = "Bahor"
yoz = "Yoz"
kuz = "Kuz"
qish = "Qish"

print(f"Fasillar: {bahor} {yoz} {kuz} {qish}")

# Maxsus belgilar. 1. \t belgisi matnga bo'shliq qo'shadi. 2. \n yangi qatordan boshlaydi.

print("Mahsus belgilarsiz matn")
print("A va B harflar orasida bo'shliq bor. A\tB")
print("Assalomu alekum \n Yangi qator.")


#  Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi.

# 1. upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 

ism1 = "ism"
familya1 = "familya"
ism_familya = f"{ism1} {familya1}"

print(ism_familya.upper())

# 2. lower() metodi esa har bir harfni kichik harfga o'zgartiradi.

ism1 = "Ism"
familya1 = "Familya"
ism_familya = f"{ism1} {familya1}"

print(ism_familya.lower())

#  3. title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 

hafta = "duyshanba seshanba"
ism_sharf = "falonchi falonchiev"

a = f"{hafta} {ism_sharf}"

print(hafta.title())
print(a.title())

"""
4. format() usuli belgilangan qiymat(lar) ni formatlaydi va ularni satrning to'ldiruvchisiga kiritadi.
To'ldiruvchi jingalak qavslar yordamida aniqlanadi: {}.
format() usuli formatlangan qatorni qaytaradi.
"""

info = "Assalomu alekum men {}, yoshim {} da"
info1 = "Assalomu alekum men {ism}, yoshim {yosh} da".format(ism = "Ali", yosh = 20)

print(info.format("Ali", 20))
print(info1)

# Raqamni ikkilik formatga aylantirish uchun "b" dan foydalaning:

txt = "{0} ning ikkilik versiyasi {0:b}" # o'nlik sanoq sistemasini ikkilik sanoq sistemasiga o'tkazadi.
print(txt.format(5))

# Raqamni foiz formatiga aylantirish uchun "%" dan foydalaning:

text = "Siz {:%} ball oldingiz."
print(text.format(0.50))

text1 = "Siz {:.0%} ball oldingiz."  #  O'nlik kasrlarsiz
print(text1.format(0.75))


"""  5. split() usuli qatorni ro'yxatga ajratadi.
string.split(separator, maxsplit)

separator:  Satrni ajratishda foydalaniladigan ajratgichni belgilaydi. Odatda, har qanday bo'sh joy ajratuvchi hisoblanadi
maxsplit:  Qancha bo'linish kerakligini belgilaydi. Standart qiymat -1, ya'ni "barcha hodisalar"
"""

# Satrni verguldan so'ng bo'sh joy qo'yib ajratuvchi sifatida ajrating:
sp = "Men, dasturlashni, o'rganyabman" # , vergul bilan ajratilgan har bir so'zni "" qo'shtirnoq ichiga oladi
b = sp.split(", ")
print(b)

#  Ajratuvchi sifatida xesh # belgisidan foydalaning:

ab = "Olma#Anor#Olcha#Behi#O'rik"
ab1 = ab.split("#")
print(ab1)


#  Satrni maksimal 2 ta elementdan iborat ro'yxatga bo'ling:

abc = "Olma#Anor#Olcha#Behi#O'rik" # maxsplit parametrini 1 ga o'rnatish, 2 ta elementdan iborat ro'yxatni qaytaradi!
abc1 = abc.split("#", 1)
print(abc1)


"""
6. join() usuli barcha elementlarni oladi va ularni bitta satrga birlashtiradi.

join() Usul takrorlanadigan ob'ektlardan satrlarni yaratishning moslashuvchan usulini ta'minlaydi.
U takrorlanadigan elementning har bir elementini (masalan, ro'yxat, satr va kortej) qator ajratuvchi
(usul chaqiriladigan satr join()) orqali birlashtiradi va birlashtirilgan qatorni qaytaradi.

string.join(iterable)
"""

sonlar = ['1', '2', '3', '4', '5']
ajratuvchu = ', '
print(ajratuvchu.join(sonlar))

s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))


test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

# 7. title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 

ism_sharif = 'james bond'
print(ism_sharif.title())

# 8. capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.

ism_sharif = 'james bond'
print(ism_sharif.title())

# lstrip() — matn boshidagi bo'shliqni,
# rstrip() – matn oxiridagi bo'shliqni,
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

"""
Python input() funksiyasi foydalanuvchi ma'lumotlarini qabul qilish uchun ishlatiladi. 
Odatda, u foydalanuvchi kiritishini satr shaklida qaytaradi.
"""

ism = input("Ismingizni kiriting: ")
print(f"Foydalanuvxhi ismi {ism}")

"""
Yuqoridagi dastur, avval 1-qatorda foydalanuvchining ismini so'raydi. 
Foydalanuvchi ismini kiritib, Enter tugmasini bosgach, foydalanuvchi kiritgan matnism degan 
o'zgaruvchiga yuklanadi va dasturining 2-qatori bajaradi:
"""


