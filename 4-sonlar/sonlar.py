#  Pythonda sonlar bilan ishlash

# INTEGERS --> Int yoki butun son - bu musbat yoki manfiy, o'nli kasrsiz, cheksiz uzunlikdagi butun son.

musbat_son = 20
manfiy_son = -40
javob = musbat_son + manfiy_son

# print(javob)

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
# print(kvdrt_yuzi)

#  FLOATS - O'NLIK SONLAR
"""
Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats deyiladi. 
"Floating point numbers" atamasini o'zbek tiliga "suzuvchi nuqtali sonlar" deb tarjima qilish mumkin.
Ingliz tilida o'nlik sonlarni yozishda vergul (,) emas nuqta (.) belgisi ishlatiladi, 
va bu nuqta sonning katta kichikligiga qarab joyi o'zgargani uchun "floating" (suzuvchi) deyiladi.

Python-dagi float funktsiyasining maqsadi haqiqiy sonlarni yoki butun sonlarni suzuvchi nuqtali raqamlarga aylantirishdir.
"""

pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
# print("Aylana uzunligi ", pi*diametr, " ga teng.")

#   ikki butun sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham)

a = -15
b = 25
c = a / b

# print(c)

#  Shuningdek butun va o'nlik sonlar o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))


"""
KONSTANTA
Aksar dasturlash tillarida konstant qiymatlar tushunchasi bor. Konstantlar o'zgarmas bo'ladi
(misol uchun ning qiymati konstant, o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, 
shuning uchun dasturchilar bunday o'zgaruvchilarning nomini katta harflar bilan yozadilar (ogohlantirish sifatida). 
Bu albatta qat'iy qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul.

PI = 3.14159
raduis = 21.2
"""

# bir nechta o'zgaruvchiga qiymat berish

a, b, c = 10, 15, 20  # bu yerda a = 10, b = 15, c = 20

# O'zgaruvchilar turini almashtirish

ism = "Ali"
yosh = 20

# natija = ism + " " + yosh  #  TypeError: can only concatenate str (not "int") to str.  matn (str) va son (int) ni jamlab bo'lmaydi 

# Pythonda matn (string) va son (int, float) turidagi o'zgaruvchilarni jamlab bo'lmaydi
# Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish uchun maxsus fumksiyalardan foydalanish mumkin.

#  str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
#  int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
#  float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

ism = "Ali"
yosh = 20

text = ism + " " + str(yosh)
print(text) 


#  O'zgaruvchi turini tekshirish.  Buning uchun type() - funksiyasidan foydalanamiz.

ism = "Ali"
yosh = 20

print(type(ism))
print(type(yosh))

# INPUT va SONLAR

# Misol-1  ❌

# t_yil = input("Tug'ilgan yilingizni kiriting: ")

# yosh = 2023 - t_yil


# Misol-2  ✅

t_yil = int(input("Tug'ilgan yilingizni kiriting: "))

yosh = 2023 - t_yil

print("Siz " + str(yosh) + " yoshdasiz")




