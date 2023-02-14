"""
for BILAN TANISHAMIZ

Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin.
Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish,
yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. 

Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. 
"""

shaxslar = ["Ali", "Vali", "Kamol", "Umar", "Soli", "Jamshid"]  # shaxslar ro'yxatini yaratildi

for shaxs in shaxslar:  # shaxslar ro'yhatidan, har bir shaxsni olib shaxs degan o'zgaruvchiga yuklayabmiz
    print(shaxs)  # yangi shaxs ro'yxatini kansolga chiqaryabmiz


#  for QANDAY ISHLAYDI

foydalanuvchilar = ["Ilhom", "Jamshid", "Umar", "Tolib", "Nodir", "Shavkat"]

for mijoz in foydalanuvchilar:
    print(f"Assalomu alekum hurmatli {mijoz} sizni Navro'z bayrami bilan tabriklaymiz.")
    print("Hurmat bilan kompaniya hodimi.\n")

"""
Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi.
Bizning holatimizda tsikl foydalanuvchilar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi.
Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.  
Tsikl badani surilish (indentation) bilan ajratiladi, ya'ni tsiklning takrorlanuvchi qismi
asosiy koddan bir muncha o'ngroqqa surilgan bo'ladi. Agar biz mana shu surilishni tark qilsak 
kodimiz xato beradi:
"""

mehmonlar = ["Ali", "Vali", "Soli"]

# for mehmon in mehmonlar:
# print(mehmon)

"""
Natija: IndentationError: expected an indented block
Ko'rib turganingizdek for dan keyingi qatorni o'ngga surmaganimiz uchun indentation error (surishda xatolik) degan xabarni oldik.
"""

"""
for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
"""

sonlar = list(range(1, 11))

for son in sonlar:
    print(son)

# -----------------------------------------------
sonlar1 = list(range(0, 5))

for son1 in sonlar1:
    print(f"{son1} ning kvadrati {son1 ** 2} ga teng")

# -------------------------------------------------

#  for yordamida yangi ro'yxat ham shakllantirish mumkin

sonlar2 = list(range(0, 6))
son_kvadrati = []

for son2 in sonlar2:
    son_kvadrati.append(son2 ** 2)
    
print(son_kvadrati)


"""
for va input()
for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar
bilan to'ldirish mumkin:
"""

dostlar = []

print("7 ta do'stingiz ismini kiriting\n")

for dos in range(0, 7):
    dostlar.append(input("Do'stingiz ismi:\n>>> "))
print(dostlar)

"""
Kodni tahlil qilamiz:
1-qatorda bo'sh dostlar ro'yxatini yaratdik
2-qatorda ekranga "7 ta do'stingiz ismini kiriting" degan xabarni chiqardik
3-qatorda tsiklni boshladik. range(0, 7) funktsiyasi 0 dan 7 gacha sonlar ketma-ketligini yaratadi (0,1,2,3,4, 5, 7) tsikl esa dos shularning har biriga teng bo'lib chiqquncha davom etadi. 
4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan Do'stingiz ismini kiriting deb so'radik.
5-qatorda shakllangan ro'yxatni konsolga chiqardik.
"""

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)


"""
Kodni tahlil qilamiz:
1-qatorda bo'sh dostlar ro'yxatini yaratdik
2-qatorda ekranga "5 ta eng yaqin do'stingiz kim?" degan xabarni chiqardik
3-qatorda tsiklni boshladik. range(5) funktsiyasi 0 dan 5 gacha sonlar ketma-ketligini yaratadi (0,1,2,3,4) tsikl esa n shularning har biriga teng bo'lib chiqquncha davom etadi. 
4-qatorda tsikl badani kelgan. Bu yerda biz foydalanuvchidan n+1 do'stingizni kiriting deb so'radik. Nima uchun n+1 (n emas)? Sababi n 0 dan 4 gacha qiymatlarni oladi, foydalanuvchiga tushunarli bo'lishi uchun esa biz "0-do'stingizni ismini kiriting:" deb emas, balki n+1 ya'ni 1-ismni kiriting deb murojat qilyapmiz.
5-qatorda shakllangan ro'yxatni konsolga chiqardik.
"""




















