"""
LIST (RO'YHAT)

Ro'yxatlar bitta o'zgaruvchida bir nechta elementlarni saqlash uchun ishlatiladi.
Ro'yxatlar Python'da ma'lumotlar to'plamini saqlash uchun ishlatiladigan 4 ta o'rnatilgan
ma'lumotlar turlaridan biri, qolgan 3 tasi Tuple , Set va Dictionary bo'lib
ularning barchasi turli sifat va foydalanishga ega.

Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash imkonini beradi.
Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlash mumkin. 
"""

# List (Ro'yxat) [] kvadrat qavslar yordamida yaratiladi

shaxslar = ['Ali', 'Vali', 'Umar', 'Soli']
sonlar = [1, 100, 12_000, 45]
aralash  = ['bir', 'ikki', 'uch', 1, 2, 3]

"""
Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan elementga uning tartib raqami 
(indeksi) bo'yicha murojat qilishimiz mumkin. 

Ro'yxat elementlari indekslanadi, birinchi element [0] indeksga ega, ikkinchi element [1] indeksga ga va hokazo.
Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi elementing tartib raqami (indeksi) 0 ga,
ikkinchi elementning indeksi 1 ga teng va hokazo.
"""

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]

# print(mevalar[0])  # mevalar ro'yhatidagi 1- element
# print(mevalar[1])  # mevalar ro'yhatidagi 2- element

#  Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]

# print(mevalar[0].lower())  
# print(mevalar[1].upper())

#  List elementlari ustida arifmetik amallar bajarish:

narhlar = [5_000, 12_000, 7_000, 18_000, 43_000]

# print(narhlar[0] + narhlar[3])  # 5_000 + 18_000 = 23_000

#    Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]

# print(mevalar[-1])


#  ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
#  Elementni o'zgartirish
#  Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, o'sha elementga indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz


narhlar = [5_000, 12_000, 7_000, 18_000, 43_000]

narhlar[0] = 10_000  # ro'yhatning birinchi elementi o'zgartirildi
narhlar[-1] = 40_000  # ro'yhatning oxirgi elementi o'zgartirildi
narhlar[2] = 8_000  # ro'yhatning 3 elementi o'zgartirildi

# print(narhlar)

#   Yangi element qo'shish

#  .append() metodi elementni ro'yxat oxiriga qo'shadi.

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]
mevalar.append("Anor")  #  ro'yhatni ohiriga Anor mevasi qo'shildi

# print(mevalar)

"""
.append() metodi bo'sh ro'yxatni to'ldrisihda juda qulay usul. 
Odatda dastur boshida bo'sh ro'yxat yaratilib, dastur davomida ro'yxat foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.
"""

mashinalar = []

mashinalar.append("BMW")
mashinalar.append("Damas")
mashinalar.append("Tico")
mashinalar.append("Nissan")

# print(mashinalar)

"""
.insert() metodi belgilangan qiymatni belgilangan joyga kiritadi.

list.insert(pos, elmnt)
pos --> Majburiy. Qiymatni qaysi pozitsiyaga kiritish kerakligini ko'rsatadigan raqam
elmnt --> Majburiy. Har qanday turdagi element (string, raqam, ob'ekt va boshqalar)
"""

tel_markalar = ["Apple", "samsung"]

tel_markalar.insert(0, "Redmi")
tel_markalar.insert(2, "Realme")

# print(tel_markalar)

#  clear() usuli ro'yxatdagi barcha elementlarni olib tashlaydi.

a = [12, 3, 45, 56]
# print(a)
# print(a.clear())


#  copy() usuli belgilangan ro'yxatning nusxasini qaytaradi.

a = [12, 3, 45, 56]
a1 = a.copy()

# print(a1)


#  count()belgilangan qiymatga ega elementlar sonini qaytaradi.

c_ount = [11, 56, 4, 11, 568, 975, 11]
# print(c_ount.count(11))  # c_ount ro'yhatida nechta 11 soni borligini chiqaradi


#  extend()  ikkita ro'yxatni bir biriga qo'shadi

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
# print(fruits)

#  index() belgilangan qiymatning indexini qaytaradi

test = [12, 5, 4545, 68, 325, 89]
# print(test.index(5))


# reverse()  ro'yhatni teskari tartiblaydi

test1 = ['ali', 'vali', 'soli']
test1.reverse()
# print(test1)


#  Elementni o'chirish
#  Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]
del mevalar[1] # 2-element (O'rik) ni o'chirib tashlaymiz
# print(mevalar)


# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. 
# Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz

mevalar = ["Olma", "O'rik", "Shaftoli", "Banan", "Gilos", "Behi"]
mevalar.remove("Olma")

# print(mevalar)

#  .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. 
# Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.


#  Elementni sug'urib olish

"""
Ba'zida biror elementni butunlay o'chirib tashlash emas, 
balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. 
Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
"""

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)

#  Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.





