"""
Avval aytganimizdek, print() funktsiyasi matn yoki ifodalarni konsolga chiqarish vazifasini bajaradi. 
Lekin bu funktsiya to'g'ri ishlashi uchun bir nechta qoidalarga amal qilish lozim. 
Jumladan, agar konsolga matn chiqarmoqchi bo'lsak, matnimiz albatta qo'shtirnoq yoki (" ") 
yoki birtirnoq(' ') orasida yozlishi kerak.
"""

print("Assalomu allekum!") # "" qo'shtirnoq ichida yozilgan matn. str

print('Hayrli tong!') # '' birtirnoq ichida yozilgan matn. str

print("Men 'Python' dasturlash tilini o'rganyabman") # tirnoqlarni '' "" ikkalasiham qatnashti. str

# Matinni qatorlarga bo'lib yozish talab qilinsa """ """ yoki ''' ''' uch tirnoqlardan yoki \n belgisidan foydalaniladi. str

print("""Yog'ayotgan yomg'ir O'rmon
daraxtlariga foda berdi.""")  #  Matn ikki qatorga bo'lib chiqariladi. str

print("Yog'ayotgan yomg'ir O'rmon \n darahtlariga foyda berdi.") # \n belgisi bilan matn ikki qatorga bo'lib yozildi.  str

"""Yog'ayotgan yomg'ir O'rmon darahtlariga foyda berdi. - bu matinni '' birtirnoqlar bilan yozmoqchi bo'lsak xatolik bo'ladi.
Buni oldini olish uchun \ belgisidan foydalanamiz. \ belgisi har qanday mahsus belgidan oldin qo'yiladi."""

print('Yog\'ayotgan yomg\'ir o\'rmon \n darahtlariga foyda berdi.') # \ belgisidan kutilgan natijano oldik. str

# ARFIMETIK AMALLAR


print(10 + 4)  # qo'shish
print(10 - 4)  # ayirish
print(10 * 4)#  ko'paytirish
print(10 / 4)  # bo'lish

print(10 // 4)  # bo'lish va butun qismini olish
print(10 ** 4)  # daraja/ildiz
print(10 % 4)  # bo'linmaning qoldig'ini olish


#  MATN VA IFODA

print("10 + 4 =",10 + 4, "ga teng")
print("10 - 4 =",10 - 4, "ga teng")
print("10 * 4 =",10 * 4, "ga teng")
print("10 / 4 =",10 / 4, "ga teng")

print("10 // 4 =",10 // 4, "ga teng")
print("10 ** 4 =",10 ** 4, "ga teng")
print("10 % 4 =",10 % 4, "ga teng")

# Izohlar (comment) #, belgisi bilan boshlanadi.